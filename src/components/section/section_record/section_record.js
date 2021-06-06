import select_service from "../../select/select_service/select_service.vue";
import select_doctor from "../../select/select_doctor/select_doctor.vue";
import select_date from "../../select/select_date/select_date.vue";
import select_time from "../../select/select_time/select_time.vue";

export default {
    name: "section_record",
    components: {
        select_service,
        select_doctor,
        select_date,
        select_time,
    },
    data() {
        return {
            default_service_form: '',
            default_doctor_form: '',
            default_date_form: '',
            default_time_form: '',
        }
    },
    methods: {
        send() {
            let counter = 0;

            document.querySelector('.modal-result-message').addEventListener('mouseover', function () {
                counter = 0;
                let interval = setInterval(() => {
                    counter -= 1;
                }, 1000);
            })

            document.querySelector('.modal-result-message').addEventListener('mouseout', function () {
                counter = 0;
                let interval = setInterval(() => {
                    counter += 1;
                }, 1000);
            })

            //управление уведомлением
            function hideMessage() {
                document.querySelector('.modal-result-message-wrapper').classList.remove('active');
            }
            document.querySelector('.start__submit').classList.add('disabled');


            document.querySelector('.close-modal').onclick = function () {
                document.querySelector('.start__submit').classList.remove('disabled');
                console.log('sdfsdfsdfs')
                clearInterval(interval);
                hideMessage();
            }

            let interval = setInterval(() => {
                counter += 1;
                console.log(counter);

                if (counter === 2) {
                    document.querySelector('.start__submit').classList.remove('disabled');
                    clearInterval(interval);
                    hideMessage();
                }

                document.querySelector('.close-modal').onclick = function () {
                    document.querySelector('.start__submit').classList.remove('disabled');
                    clearInterval(interval);
                    hideMessage();
                }
            }, 1000);


            let service_form = document.querySelector('#service_form').textContent
            let doctor_form = document.querySelector('#doctor_form').textContent
            let date_form = document.querySelector('#date_form').textContent
            let time_form = document.querySelector('#time_form').textContent

            document.querySelector('.modal-result-message-wrapper').classList.add('active');

            if (this.default_service_form === service_form || this.default_doctor_form === doctor_form || this.default_date_form === date_form || this.default_time_form === time_form) {
                document.querySelector('#modal_message').textContent = 'Пожалуйста, заполните все поля';
            } else {




                document.querySelector('#modal_message').textContent = 'Пожалуйста, введите дополнительную информацию';
                document.querySelector('.modal_wrapper').classList.toggle('active');
                setTimeout(function () {
                    document.querySelector('.modal_background').classList.toggle('active');
                }, 400);
                document.body.style.overflow = 'hidden';
            }







        },
    },
    mounted() {




        const d = document.getElementById('c');
        this.default_service_form = document.querySelector('#service_form').textContent
        this.default_doctor_form = document.querySelector('#doctor_form').textContent
        this.default_date_form = document.querySelector('#date_form').textContent
        this.default_time_form = document.querySelector('#time_form').textContent
    }
}