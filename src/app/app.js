import header_section from '../components/header/header.vue';
import footer_section from '../components/footer/footer.vue'
import modal_record from "../components/modal/modal_record.vue";

export default {
    name: 'app',
    components: {
        header_section,
        footer_section,
        modal_record,
    },
    data() {
        return {

        }
    },
    methods: {
        hideBurger() {
            document.querySelector('body').classList.toggle('active');
            document.querySelector('.toggle-menu').classList.toggle('active');
            document.querySelector('.burger-menu').classList.toggle('active');
            document.querySelector('.section_header').classList.toggle('active');
            document.querySelector('.background__dark').classList.toggle('active');
        },
    },
}