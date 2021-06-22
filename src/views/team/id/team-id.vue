<template>
    <div class="team-id">
        <div class="team-id_opacity-bg" :style="team.avatar ? {
              'background': `url(${team.avatar}) center center / cover no-repeat`
          } : {  }"></div>
        <div class="team-id__default-bg">
            <div class="team-id__header">
                Описание
            </div>
            <div class="team-id__description">
                {{team.description}}
            </div>
            <div class="team-id__row-cont">
                <div class="team-id__projects_container">
                    <h2 class="team-id__sub-title team-id__sub-title_mt-0">
                        Проекты
                        <div class="team-id__plus" @click="projectsModule.toggleOpened(true)">+</div>
                    </h2>

                    <div class="team-id__projects">
                        <div class="project_short__categories">
                            <div class="project_short__categories__name">Название</div>
                            <div class="project_short__categories__creator">Описание</div>
                            <div class="project_short__categories__actions">Участники</div>
                            <div class="project_short__categories__actions-cont"></div>
                        </div>
                        <ProjectShort
                                v-for="subteam in team.sub_teams"
                                :key="subteam.name"
                                :subteam="subteam"
                        ></ProjectShort>
                    </div>
                </div>

                <div class="team-id__members">
                    <h2 class="team-id__sub-title team-id__sub-title_mt-0 ">
                        Участники
                        <div class="team-id__plus" @click="contributorsModule.toggleAddContributor(true)">+</div>
                    </h2>

                    <div class="team-id__members__container">
                        <TeamMember
                                v-for="member in team.contributors"
                                :key="`${member.id} ${member.position.name} ${member.position.position} contributor in team`"
                                :member="member"
                                @openSettingsContributor="contributorsModule.toggleEditContributor(true, $event)"
                        >
                        </TeamMember>
                    </div>

                </div>
                <div class="team-id__button-container">
                    <BaseButton class="base-button_small">Редактировать</BaseButton>
                    <BaseButton class="base-button_small base-button_cancel" @click="tryDeleteTeam">Удалить</BaseButton>
                </div>
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
            <ModalCreateTeam
                    v-if="projectsModule.isOpened"
                    @close="projectsModule.toggleOpened(false)"
                    @save="projectsModule.addNewProject($event)"
            ></ModalCreateTeam>
            <ModalEditContributor
                    :contributor="contributorsModule.selectedContributorToEdit"
                    @save="contributorsModule.editContributorPosition"
                    @del="contributorsModule.deleteContributorFromTeam"
                    @close="contributorsModule.toggleEditContributor(false)"
                    v-if="contributorsModule.isOpenedEditContributor"
            ></ModalEditContributor>
        </teleport>

    </div>
</template>

<script>
    import {useTeam} from "../../../composition/useTeam";
    import {useRoute, useRouter} from 'vue-router'
    import {onMounted, ref, reactive} from 'vue';
    import ModalSearchProfiles from "../../../components/Modals/ModalSearchProfiles";
    import BaseButton from "../../../components/Base/BaseButton";
    import TeamMember from "../../../components/Base/TeamMember";
    import ProjectShort from "../../../components/Base/ProjectShort";
    import ModalCreateTask from "../../../components/Modals/ModalCreateTask";
    import ModalCreateTeam from "../../../components/Modals/ModalCreateTeam";
    import {useProjects} from "../../../composition/useProjects";
    import {useRouteName} from "../../../composition/useRouteName";
    import ModalEditContributor from "../../../components/Modals/ModalEditContributor";
    import {usePosition} from "../../../composition/usePosition";
    export default {
        components: {
            ModalEditContributor,
            ModalCreateTeam,
            ModalCreateTask,
            ModalSearchProfiles,
            BaseButton,
            TeamMember,
            ProjectShort
        },
        setup() {
            const { getTeam, addContributorToTeam, deleteContributorFromTeam, deleteTeam, createTeam, getTeamProjects } = useTeam();
            const { createProject } = useProjects()
            const {updatePosition} = usePosition()
            const { routeName } = useRouteName()
            const route = useRoute();
            const router = useRouter();

            const team = ref({ });
            const contributors = ref([]);
            const projects = ref([]);
            const updateTeamInfo = (newTeam) => {
                team.value = JSON.parse(JSON.stringify(newTeam));
            }

            const contributorsModule = reactive({
                isOpenedAddContributor: false,
                toggleAddContributor: (boolean) => {
                    contributorsModule.isOpenedAddContributor = boolean;
                },
                addNewContributor: ($event) => {
                    addContributorToTeam({
                        team_id: team.value.id,
                        contributor_id: $event.id,
                    })
                    .then(r => {
                        getTeam(route.params.id)
                            .then(r => {
                                updateTeamInfo(r)
                            })
                        contributorsModule.toggleAddContributor(false)
                    })
                },
                deleteContributorFromTeam: (id) => {
                    deleteContributorFromTeam({
                        team_id: team.value.id,
                        contributor_id: id,
                    })
                        .then(r => {
                            getTeam(route.params.id)
                                .then(r => {
                                    updateTeamInfo(r)
                                })
                            contributorsModule.toggleEditContributor(false);
                        })
                },
                editContributorPosition: ($event) => {
                    updatePosition({id: $event.position.id, data: {name: $event.position.name, position: $event.position.position}})
                        .then(r => {
                            getTeam(route.params.id)
                                .then(r => {
                                    updateTeamInfo(r)
                                })
                            contributorsModule.toggleEditContributor(false);
                        })
                },

                selectedContributorToEdit: null,
                isOpenedEditContributor: false,
                toggleEditContributor: (boolean, contributor = null) => {

                    if (contributor) {
                        contributorsModule.selectedContributorToEdit = contributor;
                    }

                    contributorsModule.isOpenedEditContributor = boolean;
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
                    let dataToSend = {
                        name: $event.name,
                        description: $event.description,
                        contributors_for_create: $event.contributors.map(cont => cont.id),
                        parent: team.value.id,
                    }
                    createTeam(dataToSend)
                        .then(r => {
                            getTeam(route.params.id)
                                .then(r => {
                                    updateTeamInfo(r)
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
                        updateTeamInfo(r)
                        routeName.value = team.value.name;
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

<style lang="scss" src="./team-id.scss"></style>
