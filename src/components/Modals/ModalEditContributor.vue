<template>
    <div class="modal-edit-contributor" @mousedown.self="close">
        <div class="modal-edit-contributor__body" v-if="contributor">
            <BaseModalHeader>
                {{contributorPrev.position.name}} - {{contributorPrev.profile.first_name}} {{contributorPrev.profile.last_name}}
            </BaseModalHeader>
            <div class="modal-edit-contributor__input-group">
                <BaseInput
                        class="base-input_modal base-input_mt-30"
                        placeholder="Должность"
                        v-model="contributor.position.name"
                ></BaseInput>
            </div>
            <div class="modal-edit-contributor__positions">
                <div class="modal-edit-contributor__position"
                     :class="{'modal-edit-contributor__position_active': contributor.position.position === 1}"
                     @click="changePosition(1)"
                >
                    Владелец
                </div>
                <div class="modal-edit-contributor__position"
                     :class="{'modal-edit-contributor__position_active': contributor.position.position === 2}"
                     @click="changePosition(2)"
                >
                    Заместитель
                </div>
                <div class="modal-edit-contributor__position"
                     :class="{'modal-edit-contributor__position_active': contributor.position.position === 3}"
                     @click="changePosition(3)"
                >
                    Проект-менеджер
                </div>
                <div class="modal-edit-contributor__position"
                     :class="{'modal-edit-contributor__position_active': contributor.position.position === 4}"
                     @click="changePosition(4)"
                >
                    Старший участник
                </div>
                <div class="modal-edit-contributor__position"
                     :class="{'modal-edit-contributor__position_active': contributor.position.position === 5}"
                     @click="changePosition(5)"
                >
                    Участник
                </div>
            </div>

            <div class="modal-edit-contributor__buttons">
                <BaseButton
                        class="base-button_small"
                        @click.self="save"
                >
                    Сохранить
                </BaseButton>
                <BaseButton
                        class="base-button_small base-button_cancel"
                        @click.self="del"
                >
                    Удалить
                </BaseButton>
                <BaseButton
                        class="base-button_small base-button_cancel"
                        @click.self="close"
                >
                    Закрыть
                </BaseButton>
            </div>
        </div>
    </div>
</template>

<script>
    import BaseButton from '../Base/BaseButton.vue'
    // import BaseTeamMembersShort from '../Base/BaseTeamMembersShort.vue'
    import BaseInput from '../Base/BaseInput.vue'
    import BaseModalHeader from '../Base/BaseModalHeader.vue'
    import {onMounted} from 'vue';

    import {ref} from 'vue';
    export default {
        components: { BaseButton, BaseModalHeader, BaseInput },
        props: {
            contributor: Object,
        },
        setup(props, {emit}) {
            const close = () => {
                emit('close')
            }
            const del = () => {
                emit('del', props.contributor.id)
            }
            const save = () => {
                emit('save', contributor.value);
            }
            const contributor = ref(null);
            onMounted(() => {
                contributor.value = JSON.parse(JSON.stringify(props.contributor));
            })

            const changePosition = (position) => {
                contributor.value.position.position = position;
            }

            return {
                save,
                del,
                close,
                contributor,
                contributorPrev: props.contributor,

                changePosition,
            }
        }
    }
</script>

<style lang="scss">
    .modal-edit-contributor {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(2px);
        position: absolute;
        left: 0;
        top: 0;
        color: white;
        z-index: 1300;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: left;
        &.z-index {
            z-index: 1400;
        }
    }
    .modal-edit-contributor__body {
        width: 800px;
        background: #303030;
        border-radius: 9px;
        padding: 20px;
        text-align: left;
    }
    .modal-edit-contributor__input-group {
        padding: 0 20px;
    }

    .modal-edit-contributor__contenteditable{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        font-size: 32px;
        font-weight: bold;
        background-color: transparent;

        &:focus{
            outline: none;
            border: none;
        }

    }

    .modal-edit-contributor__discription{
        color: rgb(218, 218, 218);
        margin-top: 20px;
        height: 200px;

        &:focus{
            outline: none;
            border: none;
        }
    }

    .modal-edit-contributor__buttons {
        width: 100%;
        height: 50px;
        display: flex;
        justify-content: flex-end;
        margin-top: 45px;
        align-items: center;
        .base-button{
            margin-right: 20px;
        }
    }
    .modal-edit-contributor__input-container {
        margin-top: 30px;
        padding: 0 20px;
    }
    .modal-edit-contributor__positions {
        margin-top: 30px;
        padding: 0 20px;
    }
    .modal-edit-contributor__position {
        padding: 20px;
        border: 1px solid #FFD15C;
        border-radius: 20px 10px;
        margin-bottom: 15px;
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;
        color: white;
        cursor: pointer;
        &.modal-edit-contributor__position_active {
            background: #FFD15C;
            color: #252525;
        }
    }

</style>
