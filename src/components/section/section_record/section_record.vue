<template>
    <div class="section_wrapper">
        <div class="start_form__wrapper">
            <div class="start__title">Записаться на приём</div>
            <div class="start__subtitle">по <a href="tel:89882474545">телефону</a> или онлайн</div>
            <div class="start_specialty">
                <select_service></select_service>
            </div>

            <div class="start_specialty">
                <select_doctor></select_doctor>
            </div>
            <div
                style="display: grid; grid-template-columns: 1fr 1fr; grid-gap: 28px; width: 100%; flex-wrap: wrap; position: relative; margin-bottom: 30px;">
                <div class="start_specialty_date">
                    <select_date></select_date>
                </div>
                <div class="start_specialty_date">
                    <select_time></select_time>
                </div>
            </div>
            <button type="submit" @click="send" class="start__submit"><p>Записаться</p></button>
            <div class="start__footer">
                Заполняя форму, Вы соглашаетесь с<br/><a href="#">политикой конфеденциальности</a>
            </div>
        </div>
    </div>
</template>

<script src="./section_record.js"></script>