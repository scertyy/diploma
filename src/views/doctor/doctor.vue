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
                        <div class="bread_crumbs__next">Врачи</div>
                    </div>
                </div>
            </section>
            <section class="section_outer section_service_item">
                <div class="section_inner">
                    <div class="section_wrapper">
                        <div class="section__title">Специалисты «ПРОЗДОРОВЬЕ»</div>
                        <div class="service_item__wrapper">
                            <img class="service_item__image" src="img/carteology.png" alt="" />
                            <div class="service_item__info">
                                <div class="service_item__title">Медицинская клиника «ПРОЗДОРОВЬЕ»</div>
                                <div class="service_item__description">
                                    Мы дорожим своей репутацией и это является залогом того, что лечебная услуга будет
                                    оказана качественно, в полном объёме в оптимально короткие сроки. После постановки
                                    диагноза и выдачи заключения мы предлагаем пациенту на выбор несколько вариантов
                                    лечения в соответствии именно с его ситуацией, реализуя, таким образом, его право
                                    на выбор лечения.
                                </div>
                                <div class="service_item__description">
                                    При составлении схемы лечения, помимо диагностических данных, учитывается
                                    множество других факторов (возраст, пол, общее состояние здоровья, перенесенные
                                    заболевания и хирургические вмешательства, наличие хронических заболеваний,
                                    принимаемые лекарственные средства, длительность приема, и т.д.). Вы можете быть
                                    уверены в том, что назначенное вам лечение обязательно поможет! Мы против
                                    агрессивной рекламы, поэтому занимаем «средний» сегмент стоимости услуг при
                                    неизменно высоком качестве медицинской помощи.
                                </div>

                                <button class="medic__question">Задать вопрос врачам</button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section class="section_outer section_medic_filter">
                <div class="section_inner">
                    <div class="section_wrapper">
                        <div class="medic_filter__main">
                            <div class="section__title">Врачи</div>
                            <div class="medic_filter__wrapper">
                                <div class="medic_filter__block">
                                    Выберите спициальность
                                    <svg
                                            width="13"
                                            height="7"
                                            viewBox="0 0 13 7"
                                            fill="none"
                                            xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path d="M1 1L6.5 6L12 1" stroke="#21B0BA" />
                                    </svg>
                                </div>
                                <ul class="medic_filter__menu">
                                    <li class="medic_filter__item active">Показать все</li>
                                    <li class="medic_filter__item">Гастроэнтерология</li>
                                    <li class="medic_filter__item">Гинекология</li>
                                    <li class="medic_filter__item">Кардиология</li>
                                    <li class="medic_filter__item">Лабороторные исследования</li>
                                    <li class="medic_filter__item">Неврология</li>
                                    <li class="medic_filter__item">Терапия</li>
                                    <li class="medic_filter__item">Ультразвуковая диагностика (УЗИ)</li>
                                    <li class="medic_filter__item">Эндокринология</li>
                                </ul>
                            </div>
                        </div>
                        <ul class="service_med__list">
                            <li class="service_med__item">
                                <img src="/img/med_worker.png" alt="" />
                                <div class="service_med__item_name">Афонасьева Александра Витальевна</div>
                                <div class="service_med__item_work">Глав. врач, хирург</div>
                                <div class="service_med__item_date">Опыт работы — 26 лет</div>
                                <button class="service_med__item_button">Записаться</button>
                            </li>
                            <li class="service_med__item">
                                <img src="/img/med_worker.png" alt="" />
                                <div class="service_med__item_name">Афонасьева Александра Витальевна</div>
                                <div class="service_med__item_work">Глав. врач, хирург</div>
                                <div class="service_med__item_date">Опыт работы — 26 лет</div>
                                <button class="service_med__item_button">Записаться</button>
                            </li>
                            <li class="service_med__item">
                                <img src="/img/med_worker.png" alt="" />
                                <div class="service_med__item_name">Афонасьева Александра Витальевна</div>
                                <div class="service_med__item_work">Глав. врач, хирург</div>
                                <div class="service_med__item_date">Опыт работы — 26 лет</div>
                                <button class="service_med__item_button">Записаться</button>
                            </li>
                            <li class="service_med__item">
                                <img src="/img/med_worker.png" alt="" />
                                <div class="service_med__item_name">Афонасьева Александра Витальевна</div>
                                <div class="service_med__item_work">Глав. врач, хирург</div>
                                <div class="service_med__item_date">Опыт работы — 26 лет</div>
                                <button class="service_med__item_button">Записаться</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </section>
        </main>
    </div>
</template>

<script>
    export default {
        name: "doctor"
    }
</script>

<style scoped>

</style>