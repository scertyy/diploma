<template>
    <div class="modal_record_component">
        <div>
            <div class="modal_header">
                <h3>
                    Онлайн запись на приём
                </h3>
                <p>
                    Быстрый и удобный способ регистрации на приём в клинику про-здоровье
                </p>
            </div>
            <div class="input-group-wrapper">
                <div class="input-group">
                    <input type="text" name="name" placeholder="Ваши Ф.И.О" style="order: 3;" id="input_name">
                    <input type="text" name="phone" @input="phoneMask" placeholder="Контактный телефон" class="tel"
                           style="order: 4" id="input_phone">
                    <input type="text" placeholder="Медицинский полис" style="order: 5" @input="policyMask"
                           id="policyMask"
                           maxlength="16">
                    <textarea type="text" rows="4" name="" placeholder="Комментарий" style="order: 6"
                              id="input_comment"></textarea>
                </div>
                <div class="select-modal-wrapper">
                    <div class="start_specialty" style="order: 0">
                        <select_service></select_service>
                    </div>
                    <div class="start_specialty" style="order: 1">
                        <select_doctor></select_doctor>
                    </div>
                    <div class="modal_date_select_wrapper" style="order: 2">
                        <div class="start_specialty_date">
                            <select_date></select_date>
                        </div>
                        <div class="start_specialty_date">
                            <select_time></select_time>
                        </div>
                    </div>
                    <button type="submit" class="start__submit" style="order: 7;" id="sendRequest"><p>Записаться</p>
                    </button>
                    <button type="submit" class="start__submit" style="order: 7; background: #dc3545;" id="closeModal2">
                        <p>
                            Отменить</p></button>
                    <div class="start__footer" style="order: 8;">
                        Заполняя форму, Вы соглашаетесь с<br/><a href="#">политикой конфеденциальности</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import select_service from "../select/select_service/select_service.vue";
    import select_doctor from "../select/select_doctor/select_doctor.vue";
    import select_date from "../select/select_date/select_date.vue";
    import select_time from "../select/select_time/select_time.vue";

    export default {
        name: "modal_record",
        components: {
            select_service,
            select_doctor,
            select_date,
            select_time,
        },
        mounted() {
            document.querySelector('#sendRequest').addEventListener('click', function () {
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


                let url;
                let service_form = document.querySelector('#service_form').textContent;
                let doctor_form = document.querySelector('#doctor_form').textContent;
                let date_form = document.querySelector('#date_form').textContent;
                let time_form = document.querySelector('#time_form').textContent;
                let name = document.querySelector('#input_name').value;
                let phone = document.querySelector('#input_phone').value;
                let policy = document.querySelector('#policyMask').value;
                let comment = document.querySelector('#input_comment').value;


                document.querySelector('.modal-result-message-wrapper').classList.add('active');
                if (service_form === 'Выберите специальность' || doctor_form === 'Выберите специалиста' || date_form === 'Дата' || time_form === 'Время' || name === '' || phone === '' || policy === '') {
                    document.querySelector('#modal_message').textContent = 'Пожалуйста, заполните необходимую информацию';
                } else {
                    if (policy.length < 16) {
                        document.querySelector('#modal_message').textContent = 'Неверно заполнен номер медицинского страхового полиса.';
                    }
                    else if (phone.length < 17) {
                        document.querySelector('#modal_message').textContent = 'Неверно заполнен номер телефона';
                    } else {
                        let formData = new FormData();

                        formData.append("service_form", service_form);
                        formData.append("doctor_form", doctor_form);
                        formData.append("date_form", date_form);
                        formData.append("time_form", time_form);
                        formData.append("name", name);
                        formData.append("phone", phone);
                        formData.append("policy", policy);
                        formData.append("comment", comment);

                        let xhr = new XMLHttpRequest();
                        xhr.open("POST", url)

                        try {
                            document.querySelector('.modal-result-message-wrapper').classList.add('active');
                            xhr.send(formData);
                            if (xhr.status != 200) {
                                document.querySelector('#modal_message').textContent = 'Ошибка выполнения запроса.';
                            } else {
                                document.querySelector('#modal_message').textContent = 'Запрос успешно отправлен';
                            }
                        } catch (err) { // для отлова ошибок используем конструкцию try...catch вместо onerror
                            document.querySelector('#modal_message').textContent = 'Запрос не выполнен.';
                        }
                    }
                }
            })
            document.querySelector('#modal_background').addEventListener('click', function () {
                document.querySelector('.modal_background').classList.toggle('active');
                setTimeout(function () {
                    document.querySelector('.modal_wrapper').classList.toggle('active');
                }, 400);
                document.body.style.overflow = 'visible';
            })
            document.querySelector('#closeModal2').addEventListener('click', function () {
                document.querySelector('.modal_background').classList.toggle('active');
                setTimeout(function () {
                    document.querySelector('.modal_wrapper').classList.toggle('active');
                }, 400);
                document.body.style.overflow = 'visible';
                document.querySelector('body').classList.remove('active');
                document.querySelector('.toggle-menu').classList.remove('active');
                document.querySelector('.burger-menu').classList.remove('active');
                document.querySelector('.section_header').classList.remove('active');
                document.querySelector('.background__dark').classList.remove('active');
            })
        },
        methods: {
            policyMask() {
                document.querySelector('#policyMask').value = document.querySelector('#policyMask').value.replace(/\D/g, '')
            },
            phoneMask() {
                [].forEach.call(document.querySelectorAll('.tel'), function (input) {
                    var keyCode;

                    function mask(event) {
                        event.keyCode && (keyCode = event.keyCode);
                        var pos = this.selectionStart;
                        if (pos < 3) event.preventDefault();
                        var matrix = "+7 (___) ___ ____",
                            i = 0,
                            def = matrix.replace(/\D/g, ""),
                            val = this.value.replace(/\D/g, ""),
                            new_value = matrix.replace(/[_\d]/g, function (a) {
                                return i < val.length ? val.charAt(i++) || def.charAt(i) : a
                            });
                        i = new_value.indexOf("_");
                        if (i != -1) {
                            i < 5 && (i = 3);
                            new_value = new_value.slice(0, i)
                        }
                        var reg = matrix.substr(0, this.value.length).replace(/_+/g,
                            function (a) {
                                return "\\d{1," + a.length + "}"
                            }).replace(/[+()]/g, "\\$&");
                        reg = new RegExp("^" + reg + "$");
                        if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) this.value = new_value;
                        if (event.type == "blur" && this.value.length < 5) this.value = ""
                    }

                    input.addEventListener("input", mask, false);
                    input.addEventListener("focus", mask, false);
                    input.addEventListener("blur", mask, false);
                    input.addEventListener("keydown", mask, false)

                });
            }
        }
    }
</script>

<style scoped lang="scss">
    .modal_date_select_wrapper {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 28px;
        width: 100%;
        flex-wrap: wrap;
        position: relative;
        margin-bottom: 30px;
        @media (max-width: 768px) {
            margin-bottom: 0;
        }
    }

    .input-group, .select-modal-wrapper {
        @media (max-width: 768px) {
            display: contents !important;
        }
    }

    .modal_record_component {
        position: relative;
        margin: 23px;
        @media (max-width: 768px) {
            margin: 0;
        }

        .select-modal-wrapper {
            display: flex;
            flex-direction: column;
            width: 100%;
            max-width: 404px;
            @media (max-width: 768px) {
                max-width: 100%;
            }
        }

        .modal_header {
            margin-bottom: 38px;

            h3 {
                font-family: Noah;
                font-style: normal;
                font-weight: bold;
                font-size: 38px;
                line-height: 47px;
                color: #232323;
                text-align: center;
                margin-bottom: 14px;
            }

            p {
                font-family: Noah;
                text-align: center;
                font-style: normal;
                font-weight: normal;
                font-size: 18px;
                line-height: 22px;
                color: #232323;
                margin-bottom: 21px;
            }
        }

        grid-gap: 30px;
        z-index: 1;
        background: #FFFFFF;
        border: 1px solid #EDEDED;
        border-radius: 6px;
        box-sizing: border-box;
        box-shadow: 0px 10px 12px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        /*max-height: calc(var(--vh, 1vh) * 100);*/
        height: auto;
        max-height: 100vh;
        overflow: auto;
        max-width: 1150px;
        width: 100%;
        padding: 50px 40px 60px 40px;

        &::-webkit-scrollbar {
            width: 0;
        }

        & {
            -ms-overflow-style: none;
        }

        & {
            overflow: -moz-scrollbars-none;
        }

        @media (max-width: 1360px) {
            max-width: 100%;
        }

        .input-group-wrapper {
            display: flex;
            width: 100%;
            grid-gap: 30px;
            @media (max-width: 768px) {
                flex-direction: column;
                .start_specialty {
                    margin: 0 !important;
                }
            }
        }

        .input-group {
            grid-gap: 30px;
            display: flex;
            align-items: flex-start;
            flex-direction: column;
            justify-content: flex-start;
            width: 100%;

            input, textarea {
                outline: none;
                width: 100%;
                background: #FBFBFB;
                border: 1px solid #EDEDED;
                box-sizing: border-box;
                border-radius: 6px;
                padding: 20px 30px;
                font-family: Noah;
                font-style: normal;
                font-weight: normal;
                font-size: 20px;
                line-height: 25px;
                color: #232323;
                resize: none;

                &::placeholder {
                    font-family: Noah;
                    font-style: normal;
                    font-weight: normal;
                    font-size: 20px;
                    line-height: 25px;
                    color: rgba(35, 35, 35, 0.5);
                }
            }
        }

        @media (max-width: 592px) {
            padding: 20px;
        }
    }
</style>