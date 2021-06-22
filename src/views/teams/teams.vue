<template>
    <div class="teams">
        <div class="teams__cards">
          <TeamCard
            v-for="(team, index) in teams"
            :team="team"
            :key="team.id + 'TEAM'"
            >
          </TeamCard>
        </div>

        <div class="teams__button-cont">
            <BaseButton class="base-button_small" @click="modalCreateTeam.toggleOpened(true)">Создать команду</BaseButton>
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
                return myTeams.value.filter(team => !team.is_self && !team.parent);
            })

            const modalCreateTeam = reactive({
                isOpened: false,
                toggleOpened: (boolean) => {
                    modalCreateTeam.isOpened = boolean
                },
                create: ($event) => {
                    let dataToSend = {
                        name: $event.name,
                        description: $event.description,
                        contributors_for_create: $event.contributors.map(cont => cont.id),
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

                teams,


                modalCreateTeam,
            }
        }
    }
</script>

<style lang="scss" src="./teams.scss"></style>
