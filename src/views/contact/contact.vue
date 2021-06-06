<template>
    <div>
        <main id="main">
            <section class="section_outer section_bread_crumbs">
                <div class="section_inner">
                    <div class="section_wrapper">
                        <div class="bread_crumbs__main">
                            <a href="/">Медицинская клиника «ПроЗдоровье»</a>
                        </div>
                        <div class="bread_crumbs__separator">/</div>
                        <div class="bread_crumbs__next">Контактная информация</div>
                    </div>
                </div>
            </section>
            <section class="section_outer section_service_item">
                <div class="section_inner">
                    <div class="section_wrapper">
                        <div class="section__title">Контактная информация</div>
                        <ul class="contact_buttons">
                            <a class="viev__map" href="https://yandex.ru/maps/-/CCUYqOhOwB">Показать на карте</a>
                            <li class="contact_buttons_signup">
                                <svg
                                        width="20"
                                        height="20"
                                        viewBox="0 0 20 20"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                            d="M9.77066 19.5416C4.38328 19.5416 0 15.1583 0 9.77066C0 4.38328 4.38328 0 9.77066 0C15.1583 0 19.5416 4.38328 19.5416 9.77066C19.5416 15.1583 15.1583 19.5416 9.77066 19.5416ZM9.77066 2.25481C5.62629 2.25481 2.25481 5.62629 2.25481 9.77066C2.25481 13.915 5.62629 17.2868 9.77066 17.2868C13.915 17.2868 17.2868 13.915 17.2868 9.77066C17.2868 5.62629 13.915 2.25481 9.77066 2.25481Z"
                                            fill="#232323"
                                    />
                                    <path
                                            d="M12.4018 14.7916C12.113 14.7916 11.8246 14.6818 11.6049 14.4607L8.9744 11.8302C8.76246 11.6183 8.64355 11.3326 8.64355 11.0334V6.89974C8.64355 6.27741 9.14863 5.77234 9.77096 5.77234C10.3933 5.77234 10.8984 6.27741 10.8984 6.89974V10.566L13.1983 12.866C13.6387 13.3064 13.6387 14.0203 13.1983 14.4607C12.9789 14.6818 12.6902 14.7916 12.4018 14.7916Z"
                                            fill="#232323"
                                    />
                                </svg>
                                Записаться на приём
                            </li>
                            <li class="contact_buttons_boss">
                                <svg
                                        width="18"
                                        height="25"
                                        viewBox="0 0 18 25"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                            d="M18 21.6587V16.3365C18 14.5358 16.9142 12.8652 15.1112 11.7447C15.9181 10.5442 16.3962 9.09365 16.3962 7.52302C16.3962 3.37137 13.0592 2.22066e-05 8.94521 2.22066e-05C4.85113 -0.00998179 1.50415 3.36136 1.50415 7.51302C1.50415 9.09365 1.99225 10.5642 2.81904 11.7747C1.05589 12.8952 0 14.5558 0 16.3265V21.6587H1.51411V16.3265C1.51411 15.026 2.38074 13.7855 3.8052 12.9352C4.78141 13.8756 5.99668 14.5558 7.36137 14.856L5.81738 22.439L9.00498 25L12.1926 22.439L10.6187 14.8359C11.9635 14.5258 13.1788 13.8455 14.135 12.9052C15.6093 13.7555 16.4958 15.006 16.4958 16.3265V21.6587H18ZM9.00498 23.0592L7.49087 21.8387L8.76591 15.6063H9.23409L10.5291 21.8387L9.00498 23.0592ZM8.95517 13.5154C5.68788 13.5154 3.01826 10.8243 3.01826 7.51302C3.01826 4.2017 5.67792 1.51063 8.95517 1.51063C12.2324 1.51063 14.8921 4.2017 14.8921 7.51302C14.8921 10.8243 12.2225 13.5154 8.95517 13.5154Z"
                                            fill="#232323"
                                    />
                                </svg>
                                Написать директору
                            </li>
                            <li class="contact_buttons_question">
                                <svg
                                        width="25"
                                        height="25"
                                        viewBox="0 0 25 25"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                            d="M12.1167 16.7588C11.402 16.7588 10.8232 17.3545 10.8232 18.0693C10.8232 18.7671 11.3849 19.3799 12.1167 19.3799C12.8486 19.3799 13.4273 18.7672 13.4273 18.0693C13.4273 17.3545 12.8316 16.7588 12.1167 16.7588Z"
                                            fill="#232323"
                                    />
                                    <path
                                            d="M12.3383 6.83606C10.0406 6.83606 8.98535 8.19763 8.98535 9.11672C8.98535 9.78054 9.54697 10.0869 10.0065 10.0869C10.9256 10.0869 10.5512 8.77634 12.2872 8.77634C13.1382 8.77634 13.819 9.15081 13.819 9.93372C13.819 10.8529 12.8659 11.3804 12.3042 11.857C11.8107 12.2825 11.1639 12.9803 11.1639 14.4441C11.1639 15.3291 11.4021 15.5844 12.1 15.5844C12.934 15.5844 13.1042 15.21 13.1042 14.8866C13.1042 14.0015 13.1212 13.4909 14.0573 12.7591C14.5168 12.4017 15.9636 11.2443 15.9636 9.64441C15.9636 8.04451 14.5168 6.83606 12.3383 6.83606Z"
                                            fill="#232323"
                                    />
                                    <path
                                            d="M12.5 0C5.5916 0 0 5.59067 0 12.5V24.0234C0 24.5628 0.437207 25 0.976562 25H12.5C19.4083 25 25 19.4093 25 12.5C25 5.5916 19.4093 0 12.5 0ZM12.5 23.0469H1.95312V12.5C1.95312 6.67104 6.67026 1.95312 12.5 1.95312C18.329 1.95312 23.0469 6.67026 23.0469 12.5C23.0469 18.329 18.3297 23.0469 12.5 23.0469Z"
                                            fill="#232323"
                                    />
                                </svg>
                                Задать вопрос врачам
                            </li>
                            <li class="contact_buttons_review">
                                <svg
                                        width="23"
                                        height="23"
                                        viewBox="0 0 23 23"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                            d="M20.125 0H2.875C1.28926 0 0 1.28926 0 2.875V15.8125C0 17.3982 1.28926 18.6875 2.875 18.6875H7.1875V22.4609C7.1875 22.7799 7.44805 23 7.72656 23C7.83437 23 7.94668 22.9686 8.04551 22.8922L13.6562 18.6875H20.125C21.7107 18.6875 23 17.3982 23 15.8125V2.875C23 1.28926 21.7107 0 20.125 0ZM20.8438 15.8125C20.8438 16.2078 20.5203 16.5312 20.125 16.5312H12.9375L12.3625 16.9625L9.34375 19.2266V16.5312H2.875C2.47969 16.5312 2.15625 16.2078 2.15625 15.8125V2.875C2.15625 2.47969 2.47969 2.15625 2.875 2.15625H20.125C20.5203 2.15625 20.8438 2.47969 20.8438 2.875V15.8125Z"
                                            fill="#232323"
                                    />
                                </svg>
                                Оставить отзыв
                            </li>
                        </ul>
                    </div>
                </div>
            </section>
            <section class="section_outer section_contact_info">
                <div class="section_inner">
                    <div class="section_wrapper">
                        <div class="contact_info__left">
                            Единый многоканальный телефон ПроЗдоровье:
                            <a href="tel:8 (988) 247-45-45" class="contact_info__first_tel">8 (988) 247-45-45</a>
                            <div class="contact_info__wrapper_tel">
                                Дополнительный номер телефона:
                                <a href="tel:8 (905) 472-45-45" class="contact_info__second_tel"
                                >8 (905) 472-45-45
                                </a>
                            </div>
                        </div>
                        <ul class="contact_info__right">
                            <li class="contact_info__right_item">
                                <div class="contact_info__right_title">Электронная почта:</div>
                                <ul class="contact_info__right_links">
                                    <li><a href="mailto:info@prozdorovie23.ru">info@prozdorovie23.ru</a></li>
                                </ul>
                            </li>
                            <li class="contact_info__right_item">
                                <div class="contact_info__right_title">Социальные сети:</div>
                                <ul class="contact_info__right_links">
                                    <li><a href="https://vk.com/klinika_krasnodar_prozdorovie">Вконтакте</a></li>
                                    <li><a href="https://www.instagram.com/klinika_krasnodar_prozdorovie/?hl=ru">Инстаграм</a></li>
                                </ul>
                            </li>
                            <li class="contact_info__right_item">
                                <div class="contact_info__right_title">Адрес:</div>
                                <ul class="contact_info__right_links">
                                    <li><a href="">г.Краснодар ул.Севастопольская 2, офис 44</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </section>
            <section class="section_outer section_contact_map">
                <div class="section_inner">
                    <iframe
                            src="https://yandex.ru/map-widget/v1/?um=constructor%3A4b777ad9d60b9ad90c0c1ce7a12dad91a3b608698687bde0dfabcbb8574fc8f8&amp;source=constructor"
                            width="100%"
                            height="340"
                            frameborder="0"
                    ></iframe>
                </div>
            </section>
        </main>
    </div>
</template>

<script>
    export default {
        name: "contact"
    }
</script>

<style scoped>

</style>