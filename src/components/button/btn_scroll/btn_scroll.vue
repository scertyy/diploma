<template>
    <div>
        <button class="scroll__button">
            <svg width="24" height="14" viewBox="0 0 24 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M23.3134 11.7134L12 0.400025L0.686688 11.7134L2.57202 13.6L12 4.17069L21.428 13.6L23.3134 11.7134Z"
                    fill="#0DC2B6"/>
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    name: "btn_scroll",
    methods: {

    },
    mounted() {
        const btn = document.querySelector('.scroll__button');
        btn.addEventListener('click', () => window.scrollTo({
            top: 0,
            behavior: 'smooth',
        }));

        window.addEventListener('scroll', function () {
            let currentScroll = window.pageYOffset;
            if (currentScroll > (window.screen.height / 8)) {
                document.querySelector('.scroll__button').classList.add('show_btn_scroll');
            } else {
                document.querySelector('.scroll__button').classList.remove('show_btn_scroll');
            }
        });

        window.addEventListener('scroll', function () {
            let currentScroll = window.pageYOffset;
            if (currentScroll > 100) {
                document.querySelector('#main').classList.add('scrolled');
                document.querySelector('header').classList.add('scrolled');
            } else {
                document.querySelector('#main').classList.remove('scrolled');
                document.querySelector('header').classList.remove('scrolled');
            }
        });

    }
}
</script>

<style scoped lang="scss">
.show_btn_scroll {
    opacity: 1;
    bottom: 40px;
}
</style>