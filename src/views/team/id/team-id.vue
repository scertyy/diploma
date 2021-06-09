<template>
    <div class="team-id">
        <div class="team-id__pseudo-header">
            <h1 class="team-id__name">
                {{team.name}}
            </h1>

        </div>
        <div class="team-id__container">
            <h2 class="team-id__sub-title team-id__sub-title_mt-0">
                Проекты <span class="team-id__plus" @click="projectsModule.toggleOpened(true)">+</span>
            </h2>
            <table class="team-id__contributors">
                <tr>
                    <th>Название проекта</th>
                    <th>Создатель</th>
                    <th>Действия</th>
                </tr>
                <tr v-for="project in projects" :key="project.id">
                    <td>
                        {{project.name}}
                    </td>
                    <td>
                        {{contributors.find(i => i.profile.id === project.creator).profile.first_name}}
                    </td>
                    <td>
                        <div class="team-id__actions-container">
                            <div class="team-id__contributors-action">
                                <svg width="12" height="14" viewBox="0 0 12 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M10.6293 1.40432H8.12855V0.456531C8.12855 0.204422 7.92415 0 7.67201 0H4.32809C4.07598 0 3.87156 0.204395 3.87156 0.456531V1.40432H1.37084C1.11873 1.40432 0.914307 1.60871 0.914307 1.86085V3.26514C0.914307 3.51725 1.1187 3.72168 1.37084 3.72168H1.50953L1.92679 13.5629C1.93713 13.8072 2.1383 14 2.38288 14H9.61717C9.86178 14 10.0629 13.8072 10.0733 13.5628L10.4905 3.72165H10.6292C10.8813 3.72165 11.0857 3.51725 11.0857 3.26512V1.86085C11.0858 1.60869 10.8814 1.40432 10.6293 1.40432ZM4.78462 0.913035H7.21548V1.40432H4.78462V0.913035ZM9.17964 13.087H2.82047L2.42338 3.72168H9.57667L9.17964 13.087ZM10.1727 2.80861C9.75793 2.80861 2.07587 2.80861 1.82737 2.80861V2.31736H10.1727V2.80861Z" fill="#EDEDEF"/>
                                </svg>
                            </div>
                        </div>

                    </td>
                </tr>
            </table>
        </div>
        <div class="team-id__container">
            <div class="team-id__half-container">
                <h2 class="team-id__sub-title">
                    Участники команды <span class="team-id__plus" @click="contributorsModule.toggleAddContributor(true)">+</span>
                </h2>
                <table class="team-id__contributors">
                    <tr>
                        <th>ФИО</th>
                        <th>Должность</th>
                        <th>Действия</th>
                    </tr>
                    <tr v-for="contributor in contributors" :key="contributor.id">
                        <td>
                            {{contributor.profile.first_name}} {{contributor.profile.last_name}}
                        </td>
                        <td>
                            {{contributor.position}}
                        </td>
                        <td>
                            <div class="team-id__actions-container" v-if="!contributor.is_creator">
                                <div class="team-id__contributors-action" @click="contributorsModule.deleteContributorFromTeam(contributor.id)">
                                    <svg width="12" height="14" viewBox="0 0 12 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M10.6293 1.40432H8.12855V0.456531C8.12855 0.204422 7.92415 0 7.67201 0H4.32809C4.07598 0 3.87156 0.204395 3.87156 0.456531V1.40432H1.37084C1.11873 1.40432 0.914307 1.60871 0.914307 1.86085V3.26514C0.914307 3.51725 1.1187 3.72168 1.37084 3.72168H1.50953L1.92679 13.5629C1.93713 13.8072 2.1383 14 2.38288 14H9.61717C9.86178 14 10.0629 13.8072 10.0733 13.5628L10.4905 3.72165H10.6292C10.8813 3.72165 11.0857 3.51725 11.0857 3.26512V1.86085C11.0858 1.60869 10.8814 1.40432 10.6293 1.40432ZM4.78462 0.913035H7.21548V1.40432H4.78462V0.913035ZM9.17964 13.087H2.82047L2.42338 3.72168H9.57667L9.17964 13.087ZM10.1727 2.80861C9.75793 2.80861 2.07587 2.80861 1.82737 2.80861V2.31736H10.1727V2.80861Z" fill="#EDEDEF"/>
                                    </svg>
                                </div>
                            </div>

                        </td>
                    </tr>
                </table>
            </div>
            <div class="team-id__half-container">
                <h2 class="team-id__sub-title team-id__sub-title_ta-right">
                    Задачи команды <span class="team-id__plus" @click="tasksModule.toggleOpened(true)">+</span>
                </h2>
                <table class="team-id__contributors">
                    <tr>
                        <th>Название</th>
                        <th>Исполнитель</th>
                        <th>Действия</th>
                    </tr>
                </table>
            </div>
        </div>


        <teleport to="body">
            <ModalSearchProfiles
                    v-if="contributorsModule.isOpenedAddContributor"
                    @close="contributorsModule.toggleAddContributor(false)"
                    @save="contributorsModule.addNewContributor($event)"
            ></ModalSearchProfiles>
            <ModalCreateTask
                    v-if="tasksModule.isOpened"
            ></ModalCreateTask>
            <ModalCreateProject
                    v-if="projectsModule.isOpened"
                    @close="projectsModule.toggleOpened(false)"
                    @save="projectsModule.addNewProject($event)"
            ></ModalCreateProject>
        </teleport>
        <div class="team-id__button-container">
            <BaseButton class="base-button_small" @click="tryDeleteTeam">Удалить</BaseButton>
        </div>
    </div>
</template>

<script>
    import {useTeam} from "../../../composition/useTeam";
    import {useRoute, useRouter} from 'vue-router'
    import {onMounted, ref, reactive} from 'vue';
    import ModalSearchProfiles from "../../../components/Modals/ModalSearchProfiles";
    import BaseButton from "../../../components/Base/BaseButton";
    import ModalCreateTask from "../../../components/Modals/ModalCreateTask";
    import ModalCreateProject from "../../../components/Modals/ModalCreateProject";
    import {useProjects} from "../../../composition/useProjects";
    export default {
        components: {
            ModalCreateProject,
            ModalCreateTask,
            ModalSearchProfiles,
            BaseButton
        },
        setup() {
            const { getTeam, addContributorToTeam, deleteContributorFromTeam, deleteTeam, getTeamContributor, getTeamProjects } = useTeam();
            const { createProject } = useProjects()
            const route = useRoute();
            const router = useRouter();

            const team = ref({});
            const contributors = ref([]);
            const projects = ref([]);

            const contributorsModule = reactive({
                isOpenedAddContributor: false,
                toggleAddContributor: (boolean) => {
                    contributorsModule.isOpenedAddContributor = boolean;
                },
                addNewContributor: ($event) => {
                    addContributorToTeam({
                        team_id: route.params.id,
                        profile_id: $event,
                    })
                    .then(r => {
                        getTeamContributor(route.params.id)
                            .then(r => {
                                contributors.value = [...r]
                            })
                        contributorsModule.toggleAddContributor(false)
                    })

                },
                deleteContributorFromTeam: (id) => {
                    deleteContributorFromTeam({
                        team_id: route.params.id,
                        profile_id: id,
                    })
                        .then(r => {
                            getTeamContributor(route.params.id)
                                .then(r => {
                                    contributors.value = [...r]
                                })
                        })
                }
            })
            const tasksModule = reactive({
                isOpened: false,
                toggleOpened: (boolean) => {
                    tasksModule.isOpened = boolean;
                }
            })
            const projectsModule = reactive({
                isOpened: false,
                toggleOpened: (boolean) => {
                    projectsModule.isOpened = boolean;
                },
                addNewProject: ($event) => {
                    createProject({
                        name: $event,
                        team: route.params.id,
                        creator: team.value.creator,
                    })
                        .then(r => {
                            getTeamProjects(route.params.id)
                                .then(r => {
                                    projects.value = [...r]
                                })
                            projectsModule.toggleOpened(false);
                        })
                }
            })

            const tryDeleteTeam = () => {
                deleteTeam(route.params.id)
                    .then(r => {
                        router.push('/');
                    })
            }

            onMounted(() => {
                getTeam(route.params.id)
                    .then(r => {
                        team.value = {...r}

                    })
                getTeamContributor(route.params.id)
                    .then(r => {
                        contributors.value = [...r]
                    })
                getTeamProjects(route.params.id)
                    .then(r => {
                        projects.value = [...r]
                    })

            })


            return {
                team,
                contributors,
                projects,
                tryDeleteTeam,
                tasksModule,

                contributorsModule,
                projectsModule,
            }
        }
    }
</script>

<style lang="scss">
    .team-id {
        width: 100%;
        height: 100%;
        padding: 30px;
    }
    .team-id__name {
        margin: 0;
        font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 57px;
        line-height: 72px;
        /* identical to box height */


        color: #FFFFFF;
        text-align: left;
    }
    .team-id__sub-title {
        margin: 0 0 30px;
        font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 28px;
        line-height: 36px;
        display: flex;
        align-items: center;
        /* identical to box height */

        color: #FFFFFF;
        text-align: left;
        &.team-id__sub-title_ta-right {
            justify-content: flex-end;
        }
        &.team-id__sub-title_mt-0 {
            margin: 0;
            align-self: flex-start;
            padding-right: 30px;
        }
    }
    .team-id__contributors {
        width: 100%;
        border-spacing: 0;
        background: #303030;
        padding: 10px;
        border-radius: 12px 6px;
        tr {
            border: 1px solid #FFD15C;
            box-sizing: border-box;
        }
        th {
            font-family: PT Root UI;
            font-style: normal;
            font-weight: normal;
            font-size: 20px;
            line-height: 115%;
            color: #FFFFFF;
            padding: 4px 8px;
            &:first-of-type {
                text-align: left;
            }
            &:last-of-type {
                text-align: right;
            }
        }

        td {
            font-family: PT Root UI;
            font-style: normal;
            font-weight: normal;
            font-size: 16px;
            line-height: 115%;
            color: #FFFFFF;
            padding: 4px 8px;
            &:first-of-type {
                color: #FFD15C;
                text-align: left;
            }
            &:last-of-type {
                text-align: right;
            }
        }
    }
    .team-id__pseudo-header {
        display: flex;
        width: 100%;
        justify-content: space-between;
    }
    .team-id__container {
        display: flex;
        width: 100%;
        justify-content: space-between;
        margin: 20px 0;
    }
    .team-id__half-container {
        width: 45%;
    }
    .team-id__actions-container {
        width: 100%;
        text-align: right;
        display: flex;
        justify-content: flex-end;
    }
    .team-id__contributors-action {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 22px;
        height: 22px;
        background: #FFD15C;
        border-radius: 12px 6px;
        margin-right: 5px;

        cursor: pointer;
    }

    .team-id__plus {
        margin-left: 10px;
        font-weight: bold;
        cursor: pointer;
        font-size: 36px;
    }
    .team-id__button-container {
        margin-top: 50px;
        width: 100%;
        text-align: right;
    }
</style>