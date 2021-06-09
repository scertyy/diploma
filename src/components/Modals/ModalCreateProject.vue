<template>
    <div class="modal-create-project" @mousedown.self="close">
        <div class="modal-create-project__body">
            <BaseModalHeader>
                Создать проект
            </BaseModalHeader>
            <div class="modal-create-project__input-container">
                <BaseInput class="base-input_modal" v-model="name" placeholder="Название проекта"></BaseInput>
            </div>
            <div class="modal-create-project__buttons">
                <BaseButton
                        class="base-button_small"
                        @click="save"
                >
                    Создать
                </BaseButton>
                <BaseButton
                        class="base-button_small base-button_cancel"
                        @click.self="close"
                >
                    Отмена
                </BaseButton>
            </div>
        </div>
    </div>
</template>

<script>
    import BaseButton from '../Base/BaseButton.vue'
    import BaseInput from '../Base/BaseInput.vue'
    import BaseModalHeader from '../Base/BaseModalHeader.vue'

    import {ref} from 'vue';
    export default {
        components: { BaseButton, BaseModalHeader, BaseInput },
        setup(props, {emit}) {
            const close = () => {
                emit('close')
            }
            const save = () => {
                emit('save', name.value);
            }
            const name = ref('');
            return {
                save,
                close,

                name,
            }
        }
    }
</script>

<style lang="scss">
    .modal-create-project {
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.34);
        position: absolute;
        left: 0;
        top: 0;
        z-index: 1300;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: left;
        &.z-index {
            z-index: 1400;
        }
    }
    .modal-create-project__body {
        width: 364px;
        background: #303030;
        border-radius: 9px;
        padding: 20px 0;
        text-align: left;
    }
    .modal-create-project__buttons {
        padding: 0 20px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin-top: 45px;
    }
    .modal-create-project__input-container {
        margin-top: 30px;
        padding: 0 20px;
    }

</style>