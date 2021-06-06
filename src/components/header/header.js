import btn_scroll from "../button/btn_scroll/btn_scroll.vue";

export default {
    name: "header_section",
    components: {
        btn_scroll,
    },
    data() {
        return {
            isSearchShow: false,
        }
    },
    methods: {
        showModalRecord() {
            document.querySelector('.modal_wrapper').classList.toggle('active');
            setTimeout(function () {
                document.querySelector('.modal_background').classList.toggle('active');
            }, 400);
            document.body.style.overflow = 'hidden';
        },
        showBurger() {
            document.querySelector('body').classList.toggle('active');
            document.querySelector('.toggle-menu').classList.toggle('active');
            document.querySelector('.burger-menu').classList.toggle('active');
            document.querySelector('.section_header').classList.toggle('active');
            document.querySelector('.background__dark').classList.toggle('active');
        },
        searchShow() {
            this.isSearchShow = true;
            if (document.querySelector('#search_input').value != '') {
                document.querySelector('#search_input').value = ''
            }
        },
        searchHide() {
            this.isSearchShow = false;
            if (document.querySelector('#search_input').value != '') {
                document.querySelector('.search_result').style.opacity = '0';
                setTimeout(function () {
                    document.querySelector('.search_result').style.display = 'none';
                }, 200)
                document.querySelector('#search_input').value = ''
            }
        },
        clearSearch() {
            if (document.querySelector('#search_input').value != '') {
                document.querySelector('#search_input').value = ''
            }
            document.querySelector('.search_result').style.opacity = '0';
            setTimeout(function () {
                document.querySelector('.search_result').style.display = 'none';
            }, 200)
        },
        changeHandler: function (event) {
            if (document.querySelector('.input_search > input').value != '') {
                document.querySelector('.search_result').style.display = 'block';
                setTimeout(function () {
                    document.querySelector('.search_result').style.opacity = '1';
                }, 200)
            } else {
                document.querySelector('.search_result').style.opacity = '0';
                setTimeout(function () {
                    document.querySelector('.search_result').style.display = 'none';
                }, 200)
            }
        }
    },
    mounted() {
        document.querySelector('body').addEventListener('click', function () {
            if (document.querySelector('.services_onclick') === document.activeElement) {
                document.querySelector('.service__menu_hover').classList.toggle('active')
                document.querySelector('.services_onclick > span > svg').classList.toggle('active')
            } else {
                document.querySelector('.service__menu_hover').classList.remove('active')
                document.querySelector('.services_onclick > span > svg').classList.remove('active')
            }

            if (document.querySelector('.about_onclick') === document.activeElement) {
                document.querySelector('.about__menu_hover').classList.toggle('active');
                document.querySelector('.about_onclick > span > svg').classList.toggle('active')

            } else {
                document.querySelector('.about__menu_hover').classList.remove('active');
                document.querySelector('.about_onclick > span > svg').classList.remove('active')
            }
        })
    }
}