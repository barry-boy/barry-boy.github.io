// K8s Training Home Page - Complete Redesign
document.addEventListener('DOMContentLoaded', function() {
    // 更精确的首页检测 - 只在首页生效
    const isK8sHomePage = (
        // 检查URL路径 - 包含根路径、index页面或k8s_home页面
        (window.location.pathname === '/' ||
         window.location.pathname.includes('index') ||
         window.location.pathname.includes('k8s_home') ||
         window.location.pathname === '/site/' ||
         window.location.pathname === '/site/index.html') &&
        // 检查页面标题
        (document.title?.includes('Kubernetes 进阶训练营') ||
         document.querySelector('h1')?.textContent?.includes('Kubernetes 进阶训练营课程文档'))
    );

    // 排除其他页面 - 如果URL包含这些路径，则不应用首页样式
    const isOtherPage = window.location.pathname.includes('/Docker/') ||
                       window.location.pathname.includes('/basic/') ||
                       window.location.pathname.includes('/controller/') ||
                       window.location.pathname.includes('/config/') ||
                       window.location.pathname.includes('/security/') ||
                       window.location.pathname.includes('/network/') ||
                       window.location.pathname.includes('/scheduler/') ||
                       window.location.pathname.includes('/storage/') ||
                       window.location.pathname.includes('/examples/') ||
                       window.location.pathname.includes('/helm/') ||
                       window.location.pathname.includes('/monitor/') ||
                       window.location.pathname.includes('/logging/') ||
                       window.location.pathname.includes('/devops/') ||
                       window.location.pathname.includes('/istio/') ||
                       window.location.pathname.includes('/containerd/') ||
                       window.location.pathname.includes('/skill/') ||
                       window.location.pathname.includes('/tenant/') ||
                       window.location.pathname.includes('/operator/') ||
                       window.location.pathname.includes('/0.Internet/') ||
                       window.location.pathname.includes('/1.Linux/') ||
                       window.location.pathname.includes('/2.docker/') ||
                       window.location.pathname.includes('/2.k8s/') ||
                       window.location.pathname.includes('/3.develop/') ||
                       window.location.pathname.includes('/4.database/') ||
                       window.location.pathname.includes('/5.Storage/') ||
                       window.location.pathname.includes('/6.Devops/') ||
                       window.location.pathname.includes('/7.Web/') ||
                       window.location.pathname.includes('/8.Ansible/') ||
                       window.location.pathname.includes('/9.other/') ||
                       window.location.pathname.includes('/10.Ai-tools/') ||
                       window.location.pathname.includes('/20.mylife/');

    // 只有在首页且不是其他页面时才应用特殊样式
    if (isK8sHomePage && !isOtherPage) {
        // Add body class for styling
        document.body.classList.add('k8s-home-page');

        // Wait for content to be fully loaded
        setTimeout(function() {
            createK8sHeroSection();
        }, 100);
    } else {
        // 确保其他页面不会有首页样式
        document.body.classList.remove('k8s-home-page');
    }

    function createK8sHeroSection() {
        // Find the main container
        const container = document.querySelector('.md-container');
        if (!container) return;

        // 检查是否已经存在hero section，避免重复创建
        if (document.querySelector('.k8s-hero-section')) return;

        // Create the hero section HTML
        const heroSection = document.createElement('section');
        heroSection.className = 'k8s-hero-section';
        heroSection.innerHTML = `
            <div class="k8s-hero-container">
                <div class="k8s-hero-content">
                    <h1>Kubernetes 进阶训练营课程文档</h1>
                    <p>本文档为优点知识推出的<a href="https://youdianzhishi.com/web/course/1022">《Kubernetes 进阶训练营》</a>课程文档，学完本课程以后，你将会对 Kubernetes 有一个更加深入全面的认识。</p>
                    <div class="k8s-hero-buttons">
                        <a href="https://youdianzhishi.com/web/course/1022" class="k8s-hero-button k8s-hero-button--primary">查看视频</a>
                        <a href="basic/cncf-docs/" class="k8s-hero-button">开始学习</a>
                    </div>
                </div>
                <div class="k8s-hero-image">
                    <img src="https://www.qikqiak.com/k8strain2/assets/img/illustration.png" alt="Kubernetes 训练营插图" width="1659" height="1200">
                </div>
            </div>
        `;

        // Keep the hero outside the sticky header so all pages use the same
        // header height and navigation geometry.
        container.insertBefore(heroSection, container.firstChild);

        // Add responsive behavior
        function handleResize() {
            const heroContainer = document.querySelector('.k8s-hero-container');
            const heroContent = document.querySelector('.k8s-hero-content');
            const heroImage = document.querySelector('.k8s-hero-image');

            if (heroContainer && heroContent && heroImage) {
                if (window.innerWidth <= 1220) { // 76.25em
                    heroContainer.style.flexDirection = 'column';
                    heroContainer.style.textAlign = 'center';
                    heroContainer.style.gap = '2rem';
                    heroContent.style.order = '2';
                    heroImage.style.order = '1';
                } else {
                    heroContainer.style.flexDirection = 'row';
                    heroContainer.style.textAlign = 'left';
                    heroContainer.style.gap = '4rem';
                    heroContent.style.order = '0';
                    heroImage.style.order = '0';
                }
            }
        }

        // Initial call and event listener
        handleResize();
        window.addEventListener('resize', handleResize);
    }
});
