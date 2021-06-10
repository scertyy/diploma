<template>
    <div class="modal-create-team" @mousedown.self="close">
        <div class="modal-create-team__body">
            <BaseModalHeader>
                Создать команду
            </BaseModalHeader>
            <div class="modal-create-team__input-container">
                <BaseInput class="base-input_modal" v-model="name" placeholder="Название"></BaseInput>
            </div>

            <BaseTeamMembersShort class="team_members_short__modal"></BaseTeamMembersShort>
            <BaseCardProjects class="card__projects__modal"></BaseCardProjects>

            <div class="modal-create-team__buttons">
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
    import BaseTeamMembersShort from '../Base/BaseTeamMembersShort.vue'
    import BaseModalHeader from '../Base/BaseModalHeader.vue'
    import BaseCardProjects from '../Base/BaseCardProjects.vue'

    import {ref} from 'vue';
    export default {
        components: { BaseButton, BaseModalHeader, BaseInput, BaseTeamMembersShort, BaseCardProjects },
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
    .modal-create-team {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(2px);
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
    .modal-create-team__body {
        width: 600px;
        height: 500px;
        background: #303030;
        border-radius: 9px;
        padding: 30px 20px;
        text-align: left;
    }
    .modal-create-team__buttons {
        padding: 0 20px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin-top: 45px;
    }
    .modal-create-team__input-container {
        margin-top: 30px;
        padding: 0 20px;
    }

</style>
