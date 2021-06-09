<template>
    <div class="teams">
        <div class="teams__button-cont">
            <BaseButton @click="modalCreateTeam.toggleOpened(true)">Создать команду</BaseButton>
        </div>
        <div class="teams__teams-table">
            <router-link :to="`/team/${i.id}`" class="teams__teams-element" v-for="i in myTeams" :key="i.id">
                <div class="teams__teams-row">
                    <div class="teams__teams-name teams__teams-name_small">
                        Название:
                    </div>
                    <div class="teams__teams-name teams__teams-name_align-right">
                        {{i.name}}
                    </div>
                </div>
                <div class="teams__teams-row">

                    <div class="teams__teams-name teams__teams-name_small">
                        Сотрудников:
                    </div>
                    <div class="teams__teams-name teams__teams-name_align-right">
                        {{i.count_of_contributors}}
                    </div>
                </div>

            </router-link>
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
    import {onMounted, reactive} from 'vue'
    import BaseButton from '../../components/Base/BaseButton'
    import ModalCreateTeam from '../../components/Modals/ModalCreateTeam'
    import {useProfile} from "../../composition/useProfile";

    export default {
        components: {
            BaseButton,
            ModalCreateTeam
        },
        setup() {
            const { getMyTeams, myTeams, createTeam } = useTeam()
            const { profile } = useProfile()


            onMounted(() => {
                getMyTeams()
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

<style lang="scss">
    .teams {
        width: 100%;
        height: 100%;
    }
    .teams__button-cont {
        margin: 30px 0;
    }
    .teams__teams-table {
        width: 100%;
        padding: 30px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .teams__teams-element {


        background: #303030;
        border-radius: 32px 16px;
        padding: 20px;
        width: 300px;
        margin-bottom: 30px;
        flex-shrink: 0;
        box-shadow: 0px 4px 0px #303030;
        transition: .2s ease;
        &:hover {
            box-shadow: 0px 4px 0px #4cce59;
        }
        cursor: pointer;

        text-decoration: none;
    }
    .teams__teams-row {
        width: 100%;

        text-align: left;
        display: flex;
        justify-content: space-between;
        margin-bottom: 15px;
    }
    .teams__teams-name {
        color: #FFFFFF;
        font-style: normal;
        font-weight: bold;
        font-size: 18px;
        line-height: 115%;
        /* or 25px */

        text-align: center;
        &.teams__teams-name_small {
            font-size: 14px;
        }
        &.teams__teams-name_align-right {
            text-align: right;
        }
    }
</style>