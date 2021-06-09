<template>
    <div class="team-id">
        <div class="team-team_id__projects_container">
            <h2 class="team-id__sub-title team-id__sub-title_mt-0">
                Проекты
                <div class="team-id__plus" @click="projectsModule.toggleOpened(true)">+</div>
            </h2>

            <div class="team_id__projects">
              <div class="project_short__categories">
                <div class="project_short__categories__name">Name</div>
                <div class="project_short__categories__creator">Creator</div>
                <div class="project_short__categories__actions">Actions</div>
              </div>
              <ProjectShort
                v-for="one in ones"
                :key="one.name"
                :name="one.name"
                :creator="one.creator"
                :action="one.actions"
              ></ProjectShort>
            </div>
        </div>

        <div class="team-team_id__members">
          <h2 class="team-id__sub-title team-id__sub-title_mt-0">
              Участники
              <div class="team-id__plus" @click="projectsModule.toggleOpened(true)">+</div>
          </h2>

          <div class="team-team_id__members__container">
            <TeamMember
              v-for="member in members"
              :key="member.name"
              :name="member.name"
              :photo="member.photo"
            >
            </TeamMember>
          </div>

        </div>
        <!-- <div class="team-id__container">
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
        </div> -->


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
    import TeamMember from "../../../components/Base/TeamMember";
    import ProjectShort from "../../../components/Base/ProjectShort";
    import ModalCreateTask from "../../../components/Modals/ModalCreateTask";
    import ModalCreateProject from "../../../components/Modals/ModalCreateProject";
    import {useProjects} from "../../../composition/useProjects";
    export default {
        components: {
            ModalCreateProject,
            ModalCreateTask,
            ModalSearchProfiles,
            BaseButton,
            TeamMember,
            ProjectShort
        },

        data(){
          return {
            members: [
              {
                name: "Роман Романович",
                photo: 'roman'
              },
              {
                name: "Кирилл Кириллович",
                photo: 'kirill'
              }
            ],
            // Ones — список проектов, projects уже было занято
            ones: [
              {
                name: "Пупа и Лупа",
                creator: {
                  name: "Роман",
                  photo: "roman",
                },
                actions: {
                  author: 'roman',
                  comment: 'Пришёл в бухгалтерию'
                }
              },
              {
                name: "Шляпа",
                creator: {
                  name: "Кирилл",
                  photo: "kirill",
                },
                actions: {
                  author: 'kirill',
                  comment: 'Ему как раз'
                }
              },
              {
                name: "Диплом",
                creator: {
                  name: "Роман",
                  photo: "roman",
                },
                actions: {
                  author: 'roman',
                  comment: 'Получил 5'
                }
              }
            ]
          }
        },
        setup() {
            const { getTeam, addContributorToTeam, deleteContributorFromTeam, deleteTeam, getTeamContributor, getTeamProjects } = useTeam();
            const { createProject } = useProjects()
            const route = useRoute();
            const router = useRouter();

            const team = ref({
                count_of_contributors: 3,
                creator: 1,
                id: 2,
                name: "ВКР",
            });
            const contributors = ref([{
                id: 1,
                is_creator: true,
                position: "Владелец",
                profile: {
                    id: 1,
                    first_name: "Ким",
                    last_name: "Сергей",
                    email: "sw1ple@mail.ru",
                    profile_pic: null,
                    teams: [2, 3],
                    username: "scertyy",
                },
                team: 2,
            }, {
                id: 2,
                is_creator: false,
                position: "Участник",
                profile: {
                    id: 2,
                    first_name: "Гей",
                    last_name: "Сергей",
                    email: "sw1ple@mail.ru",
                    profile_pic: null,
                    teams: [2, 3],
                    username: "scertyy",
                },
                team: 2,
            }, {
                id: 3,
                is_creator: false,
                position: "Участник",
                profile: {
                    id: 3,
                    first_name: "Не Гей",
                    last_name: "Сергей",
                    email: "sw1ple@mail.ru",
                    profile_pic: null,
                    teams: [2, 3],
                    username: "scertyy",
                },
                team: 2,
            }]);
            const projects = ref([{
                creator: 1,
                id: 1,
                name: "новый проект",
                team: 2,
            }]);

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
                // getTeam(route.params.id)
                //     .then(r => {
                //         team.value = {...r}
                //     })
                // getTeamContributor(route.params.id)
                //     .then(r => {
                //         contributors.value = [...r]
                //     })
                // getTeamProjects(route.params.id)
                //     .then(r => {
                //         projects.value = [...r]
                //     })

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
