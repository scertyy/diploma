<template>
    <div class="modal_edit_task" @mousedown.self="close">
        <div class="modal_edit_task__body">

            <div contenteditable class="modal_edit_task__contenteditable" name="name" rows="1" cols="30">Покормить рыбок</div>

            <div contenteditable class="modal_edit_task__discription">
              Покормить кормом из красной коробочки с белой этикеточкой. Не перепутать с белой коробочкой с красной крышечкой! В ней яд для тараканов.
            </div>


            <div class="modal_edit_task__buttons">
              <BaseTeamMembersShort :members="members" class="team_members_short__edit_task_modal"></BaseTeamMembersShort>
                <BaseButton
                        class="base-button_small base-button_cancel"
                        @click.self="save"
                >
                    Закрыть
                </BaseButton>
            </div>
        </div>
    </div>
</template>

<script>
    import BaseButton from '../Base/BaseButton.vue'
    import BaseTeamMembersShort from '../Base/BaseTeamMembersShort.vue'
    import BaseInput from '../Base/BaseInput.vue'
    import BaseModalHeader from '../Base/BaseModalHeader.vue'

    import {ref} from 'vue';
    export default {
        components: { BaseButton, BaseModalHeader, BaseTeamMembersShort, BaseInput },
        data(){
          return {
            members: [
              {
                name: "Роман Хмелев",
                photo: 'roman'
              },
              {
                name: "Кирилл Козырев",
                photo: 'kirill'
              },
              {
                name: "Сергей Ким",
                photo: 'sergei'
              }
            ]
          }
        },
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
    .modal_edit_task {
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
    .modal_edit_task__body {
        width: 800px;
        background: #303030;
        border-radius: 9px;
        padding: 20px;
        text-align: left;
    }

    .modal_edit_task__contenteditable{
      font-family: Avenir, Helvetica, Arial, sans-serif;
      font-size: 32px;
      font-weight: bold;
      background-color: transparent;

      &:focus{
        outline: none;
        border: none;
      }

    }

    .modal_edit_task__discription{
      color: rgb(218, 218, 218);
      margin-top: 20px;
      height: 200px;

      &:focus{
        outline: none;
        border: none;
      }
    }

    .modal_edit_task__buttons {
        width: 100%;
        height: 50px;
        display: flex;
        justify-content: flex-end;
        margin-top: 45px;
        align-items: center;
    }
    .modal_edit_task__input-container {
        margin-top: 30px;
        padding: 0 20px;
    }

</style>
