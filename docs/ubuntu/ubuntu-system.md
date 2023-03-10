
## **系统安装**
正所谓不会装系统的运维就不是好运维的理念，下面介绍一下ubuntu系统安装

!!! info "准备工作"
    - 步骤一: 下载iso镜像
        - 下载地址: https://mirrors.aliyun.com/ubuntu-releases/
    - 步骤二: 制作系统盘
        - 可以参考使用技巧中的Mac制作系统盘这篇文章
    - 步骤三: 装就完事了

1.1. 选择语言
![第一步](https://pic.imgdb.cn/item/632d192516f2c2beb1185a77.png)

1.2. 选择键盘（本步骤直接默认按回车即可。）
![第二步](https://pic.imgdb.cn/item/632d192616f2c2beb1185a80.png)

1.3. 配置网络（一般情况会直接跳过这一步）
![第三步](https://pic.imgdb.cn/item/632d192616f2c2beb1185a8b.png)

1.4. 选择代理（默认回车跳过）
![第四步](https://pic.imgdb.cn/item/632d192616f2c2beb1185a94.png)

1.5. 配置镜像源（跳过）

1.6. 选择磁盘（这个步骤比较关键）
![第五步](https://pic.imgdb.cn/item/632d192616f2c2beb1185a9e.png)

选择磁盘这一步需要注意，需要所有磁盘空间分给根分区
![第五步](https://pic.imgdb.cn/item/632d193416f2c2beb1186a6c.png)

![第五步](https://pic.imgdb.cn/item/632d193416f2c2beb1186a7d.png)


1.7. 用户信息
![第六步](https://pic.imgdb.cn/item/632d193416f2c2beb1186a90.png)


1.8. openssh server 切记要选择上 (`切记`)
![第七步](https://pic.imgdb.cn/item/632d193416f2c2beb1186aa0.png)



## **系统初始化**

!!! tip "初始化步骤"
    - 添加hosts信息

    - 修改国内apt源
        - 清华源
        - 阿里源
    - 添加管理员用户
        - 通常几个管理人员几个管理用户
    - 修改内核参数
    - 安装基础软件，gpu驱动
    - 安装docker
        - 安装容器运行时
    - 安装kubernetes
        - 安装指定kubeadm版本

以上初始化可以通过跑ansible来实现，下面具体拆分来配置一下



!!! warning "温馨提示"
    - 以下操作系统版本是以最新的ubuntu22.04 为例子来演示

### **更换国内源**

!!! info "ubuntu22.04 清华源"
    - 需要注意一下，如果apt update 报错，就将https改成http
    - 如果需要添加其他的版本的源可以访问: https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
    ```
    # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

    # 预发布软件源，不建议启用
    # deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
    ```








## **安全**

### **五: 系统安全**

通常在企业中，服务器会遭受外来的很多的恶意攻击，那么服务器的安全就显得格外的重要。首先肯定想到的是服务器的帐号和密码管理，通常的情况下会禁止root这样的管理员用户登陆，也会禁止密码这样的方式登陆。

**原因:**
  
  - root用户的权限太高，如果一旦帐号密码泄漏，就会造成很严重的后果。
  
  - 禁止密码方式登陆也是为了安全考虑，毕竟密码丢失也是很平常的事情。推荐使用公钥的方式来登陆服务器。


#### **5.1: 禁止root用户:** （centos/ubuntu都适用）
  
  - 可以修改`/etc/ssh/sshd_config`配置文件
  - 添加: `PermitRootLogin yes` 配置（一般情况下，在完成初始化就禁止root登陆了）
    - yes 为允许root登陆
    - no  为禁止root登陆
  - 重新启动sshd服务。`systemctl restart sshd`
  - 当然也可以加入系统初始化步骤中，略～


#### **5.2: 密钥对来登陆服务器**

生成公钥和私钥
```shell
root@user:~# ssh-keygen   //一路回车
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:J0s/ZHIRTj/UCcDQLHtxd5Qa0p3r2CYlcz7lPS7VaXU root@user
The key's randomart image is:
+---[RSA 3072]----+
|        .=+.+o.o+|
|        .o==.o++.|
|         ooo+.o..|
|        . .. = +E|
|        S.=   X.B|
|       . X   o @+|
|        . o   * o|
|           . . . |
|              .  |
+----[SHA256]-----+
```

这个时候在.ssh目录下生成几个文件

```shell
root@user:~# ll .ssh/
total 16
drwx------ 2 root root 4096 Sep 20 09:46 ./
drwx------ 5 root root 4096 Sep 20 09:35 ../
-rw------- 1 root root    0 May 24 15:30 authorized_keys  // 这个是授权文件
-rw------- 1 root root 2590 Sep 20 09:46 id_rsa         // 这个是私钥文件
-rw-r--r-- 1 root root  563 Sep 20 09:46 id_rsa.pub    //这个是公钥文件
```

将公钥加入user用户下: `.ssh/authorized_keys`

```shell
root@user:/home/user# ls -a .ssh/
.  ..  authorized_keys
root@user:/home/user# cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDwWSc73tyq4TAkXxt3rWmGggbpgdm+egc8mOSDu0hauuvPdieIe1qUbKsIKC1O93KyDPlsfP5gcwqdEmf5Di0S6CCxRh6ENyZ9mtN+s1pCDeHiKbjhPyG4o71tafIDOjhcbpEtCwPA0YTrp5i1oO466qYHeFmTCmkcDFhuEKZx78EZdTwbFH0vhOGTymLFgUVauzmd45ZxpTzaZHrd093nFHWg6FeZWk2axkDiijLALNxiAAaECn2S69y5SxXgKSqpe4Z25b2cKKySlM1lBv1eI7CSxAUoxuXSpcgoRiVUx5VgJwkixKvq8NpihYEkV5pFRjB8W0ssu1YF6d+3MlzOkwa+kir9JJlLq+F/rrBTfF2mCLBgg0KE+voDd8vjEkqSmweNs2gEO7Gi/fUEfcabNAOuNNPL2dhdFl+BH2TCofDYvZcWd8Wrl/0qoW5nbUdCaC7aznb0lpVgseB/gj6ah3adCzfA/W8S+1znD9VMHDdMNy+AN8eeQQ6d2t05SOc=
```
话不多说测试登陆

```shell
$ ssh user@172.30.42.244    //这是我们使用user用户登陆，就不需要密码了
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-113-generic x86_64)
```

!!! tip "禁止用户密码登陆"
    - 为了安全的考虑，我们需要关闭用户密码登陆的这种方式
    ```shell
    PubkeyAuthentication yes    # 启用公告密钥配对认证方式 
    RSAAuthentication yes       # 允许RSA密钥
    PasswordAuthentication no   # 禁止密码验证登录,如果启用的话,RSA认证登录就没有意义了
    PermitRootLogin no          # 禁用root账户登录，非必要，但为了安全性，请配置
    ```
    - 这样结合上一步骤，关闭用户账号密码验证方式，只采用密钥对会安全很多。







!!! fail "SSH 无法登陆"
    - 可以ping通但无法ssh
    - ssh -v ip 无明显报错
    - 考虑是否是服务端禁止客户端
    - 在/etc/hosts.allow文件中加上  sshd: ALL ，重启sshd

!!! info "修改网卡配置"
    
```
root@ubuntu:/home/ubuntu# cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens18:
      addresses:
      - 192.168.1.114/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
        - 192.168.1.1
        search:
        - 202.106.46.151
  version: 2
```

!!! info "清除内核缓存"
    https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/


## **Ubuntu 系统管理 && 安装及管理程序:**

### **dpkg 包安装**

#### **（1）格式**
- dpkg [选项] 包文件

#### **（2）用法**


| 参数      | Description                          |
| ----------- | ------------------------------------ |
| - i      |  安装 deb 软件包  |
| - r       | 删除 deb 软件包 |
| -r --purge     | 连同配置文件一起删除 |
|  -l   | 查看系统中已安装软件包信息  |
|  -p  | 卸载软件包及其配置文件，但无法解决依赖关系 |


#### **（3）辅助选项**
--force-all  强制安装一个包(忽略依赖及其它问题)



### **apt 包安装 卸载**

#### **（1）格式**
apt [options] [command] [package ...]

#### **（2）用法**

apt install -y  package_name  //安装

apt remove  package_name   //卸载

apt update  //列出所有可更新的软件清单命令




#### **（3）案例**

```shell
// 过滤出来以rc开头和nvidia的包并卸载
dpkg -l |grep nvidia |grep "^rc" |awk '{print $2}' |grep -E 'nvidia' | xargs dpkg  --purge

dpkg -l |grep nvidia |grep "^ii" |awk '{print $2}' |grep -E '^nvidia' | xargs dpkg --force-all  -r
```





#### **附件:**
  - 文章地址: [ubuntu安装参考:](https://www.cnblogs.com/mefj/p/14964416.html) 