<template>
    <div class="teams">
        <div class="teams__cards">
          <TeamCard
            v-for="(team, index) in myTeams"
            :key="index"
            :name="index"
            :projects="team.projects"
            :members="team.members"
            >
          </TeamCard>
        </div>

        <div class="teams__button-cont">
            <BaseButton @click="modalCreateTeam.toggleOpened(true)">Создать команду</BaseButton>
        </div>

        <teleport to="body">
            <ModalCreateTeam
                    v-if="modalCreateTeam.isOpened"
                    @close="modalCreateTeam.toggleOpened(false)"
                    @save="modalCreateTeam.create($event)"
            ></ModalCreateTeam>
        </teleport>
    </div>
</template>


<script>
    import {useTeam} from "../../composition/useTeam";
    import {onMounted, reactive, computed} from 'vue'
    import TeamCard from '../../components/Base/TeamCard.vue'
    import BaseButton from '../../components/Base/BaseButton'
    import ModalCreateTeam from '../../components/Modals/ModalCreateTeam'
    import {useProfile} from "../../composition/useProfile";
    import {useRouteName} from "../../composition/useRouteName";

    export default {
        // data(){
        //   return {
        //     teams: {
        //       'Big Boys': {
        //         members: [
        //           {
        //             name: "Роман Хмелев",
        //             photo: 'roman'
        //           },
        //           {
        //             name: "Кирилл Козырев",
        //             photo: 'kirill'
        //           },
        //           {
        //             name: "Сергей Ким",
        //             photo: 'sergei'
        //           }
        //         ],
        //         projects: [
        //           {
        //             name: "Пупа и Лупа",
        //             creator: {
        //               name: "Роман",
        //               photo: "roman",
        //             },
        //             actions: {
        //               author: 'kirill',
        //               comment: 'Пришёл в бухгалтерию'
        //             }
        //           },
        //           {
        //             name: "Шляпа",
        //             creator: {
        //               name: "Кирилл",
        //               photo: "kirill",
        //             },
        //             actions: {
        //               author: 'kirill',
        //               comment: 'Ему как раз'
        //             }
        //           },
        //           {
        //             name: "Диплом",
        //             creator: {
        //               name: "Сергей",
        //               photo: "sergei",
        //             },
        //             actions: {
        //               author: 'sergei',
        //               comment: 'Получил 5'
        //             }
        //           },
        //           {
        //             name: "Очень важный проект",
        //             creator: {
        //               name: "Сергей",
        //               photo: "sergei",
        //             },
        //             actions: {
        //               author: 'sergei',
        //               comment: 'Получил 5'
        //             }
        //           },
        //           {
        //             name: "Ёжики",
        //             creator: {
        //               name: "Сергей",
        //               photo: "sergei",
        //             },
        //             actions: {
        //               author: 'sergei',
        //               comment: 'Получил 5'
        //             }
        //           }
        //         ]
        //       },
        //       'Simple Dimple': {
        //         members: [
        //           {
        //             name: "Роман Хмелев",
        //             photo: 'roman'
        //           },
        //           {
        //             name: "Сергей Ким",
        //             photo: 'sergei'
        //           }
        //         ],
        //         projects: [
        //           {
        //             name: "Пупа и Лупа",
        //             creator: {
        //               name: "Роман",
        //               photo: "roman",
        //             },
        //             actions: {
        //               author: 'kirill',
        //               comment: 'Пришёл в бухгалтерию'
        //             }
        //           },
        //           {
        //             name: "Диплом",
        //             creator: {
        //               name: "Сергей",
        //               photo: "sergei",
        //             },
        //             actions: {
        //               author: 'sergei',
        //               comment: 'Получил 5'
        //             }
        //           }
        //         ]
        //       },
        //       'WEB NOOBS': {
        //         members: [
        //           {
        //             name: "Кирилл Козырев",
        //             photo: 'kirill'
        //           },
        //           {
        //             name: "Сергей Ким",
        //             photo: 'sergei'
        //           }
        //         ],
        //         projects: [
        //           {
        //             name: "Пупа и Лупа",
        //             creator: {
        //               name: "Роман",
        //               photo: "roman",
        //             },
        //             actions: {
        //               author: 'kirill',
        //               comment: 'Пришёл в бухгалтерию'
        //             }
        //           },
        //           {
        //             name: "Шляпа",
        //             creator: {
        //               name: "Кирилл",
        //               photo: "kirill",
        //             },
        //             actions: {
        //               author: 'kirill',
        //               comment: 'Ему как раз'
        //             }
        //           },
        //           {
        //             name: "Диплом",
        //             creator: {
        //               name: "Сергей",
        //               photo: "sergei",
        //             },
        //             actions: {
        //               author: 'sergei',
        //               comment: 'Получил 5'
        //             }
        //           }
        //         ]
        //       }
        //     }
        //   }
        // },

        components: {
            BaseButton,
            TeamCard,
            ModalCreateTeam
        },
        setup() {
            const { getMyTeams, myTeams, createTeam } = useTeam()
            const { routeName } = useRouteName()
            const { profile } = useProfile()


            onMounted(() => {
                getMyTeams();
                routeName.value = 'Мои команды'
            })

            const teams = computed(() => {

            })

            const modalCreateTeam = reactive({
                isOpened: false,
                toggleOpened: (boolean) => {
                    modalCreateTeam.isOpened = boolean
                },
                create: ($event) => {
                    let dataToSend = {
                        name: $event,
                        creator: profile.value.id,
                    }
                    createTeam(dataToSend)
                        .then(r => {
                            if (r.id) {
                                modalCreateTeam.toggleOpened(false);
                                getMyTeams()
                            }
                        })
                }
            })

            return {
                myTeams,


                modalCreateTeam,
            }
        }
    }
</script>

<style lang="scss" src="./teams.scss"></style>
