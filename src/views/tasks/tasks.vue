<template>
    <div class="tasks">
        <draggable
                class="tasks__row"
                :list="boards"
                group="board"
                itemKey="name"
                @change="log"
        >
            <template #item="{ element, index }">
                <div class="tasks__column">
                    <h3 class="tasks__board-name">
                        {{element.name}}
                        <svg style="cursor: pointer" @click="openEditDashboard(element.id)" width="33" height="35" viewBox="0 0 33 35" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M31.251 10.1771L30.1768 8.32286C29.268 6.75385 27.254 6.21258 25.6745 7.11286V7.11286C24.9227 7.55343 24.0255 7.67843 23.1809 7.46028C22.3364 7.24214 21.6137 6.69877 21.1723 5.95C20.8883 5.47407 20.7357 4.93199 20.73 4.37857V4.37857C20.7556 3.49131 20.4191 2.63151 19.7971 1.99504C19.1751 1.35857 18.3206 0.999634 17.4283 1H15.2641C14.3899 0.99999 13.5517 1.34651 12.935 1.96289C12.3184 2.57927 11.974 3.41469 11.9782 4.28429V4.28429C11.9523 6.07971 10.4817 7.52161 8.67661 7.52143C8.12027 7.51568 7.57533 7.3639 7.09688 7.08143V7.08143C5.51742 6.18115 3.50344 6.72242 2.59465 8.29143L1.44144 10.1771C0.533753 11.7442 1.07048 13.7463 2.64204 14.6557V14.6557C3.66358 15.2424 4.29288 16.3266 4.29288 17.5C4.29288 18.6734 3.66358 19.7576 2.64204 20.3443V20.3443C1.07247 21.2475 0.535163 23.2448 1.44144 24.8071V24.8071L2.53146 26.6771C2.95726 27.4414 3.67169 28.0054 4.51665 28.2443C5.36162 28.4832 6.26744 28.3773 7.03369 27.95V27.95C7.78696 27.5128 8.68459 27.393 9.52707 27.6173C10.3695 27.8415 11.0871 28.3913 11.5201 29.1443C11.8041 29.6202 11.9567 30.1623 11.9625 30.7157V30.7157C11.9625 32.5296 13.4406 34 15.2641 34H17.4283C19.2456 34 20.7213 32.5392 20.73 30.7314V30.7314C20.7257 29.8591 21.0722 29.0213 21.6923 28.4044C22.3124 27.7876 23.1547 27.4429 24.0316 27.4471C24.5866 27.4619 25.1293 27.6131 25.6113 27.8871V27.8871C27.1867 28.7901 29.1994 28.2562 30.1136 26.6929V26.6929L31.251 24.8071C31.6912 24.0554 31.8121 23.1602 31.5867 22.3196C31.3614 21.479 30.8084 20.7624 30.0504 20.3286V20.3286C29.2923 19.8947 28.7394 19.1782 28.514 18.3376C28.2887 17.497 28.4095 16.6017 28.8498 15.85C29.1361 15.3528 29.5505 14.9405 30.0504 14.6557V14.6557C31.6125 13.7468 32.148 11.7564 31.251 10.1929V10.1929V10.1771Z" stroke="#A7A7A7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <ellipse cx="16.3543" cy="17.4998" rx="4.54962" ry="4.52571" stroke="#A7A7A7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </h3>

                    <draggable
                            :list="element.list"
                            group="tasks"
                            itemKey="id"
                            @change="log"
                    >
                        <template #item="{ element, index }">
                            <div class="tasks__item" @click="modalEditTasksModule.toggleOpened(true)">{{ element.name }}</div>
                        </template>
                        <template #footer>
                            <div class="tasks__item tasks__item_create">Создать</div>
                        </template>
                    </draggable>
                </div>
            </template>
        </draggable>

        <teleport to="body">
            <ModalEditTask
                v-if="modalEditTasksModule.isOpened"
            ></ModalEditTask>
        </teleport>

    </div>
</template>
<script>
    import draggable from "vuedraggable";
    import {reactive, computed, ref} from 'vue'
    import ModalEditTask from "../../components/Modals/ModalEditTask";
    export default {
        components: {
            ModalEditTask,
            draggable
        },
        setup() {
            const boards = reactive({
                data: [
                {
                    name: 'Первая доска',
                    id: 1,
                    list: [
                        { name: "Покушать", id: 1 },
                        { name: "Покормить собаку", id: 2 },
                        { name: "Написать вкр", id: 3 },
                        { name: "Поспать", id: 4 }
                    ],
                },
                {
                    name: 'Вторая доска',
                    id: 2,
                    list: [
                        { name: "Покормить рыбок", id: 5 },
                        { name: "Сходить за продуктами", id: 6 },
                        { name: "Сойти с ума", id: 7 }
                    ]
                }]
            })
            const clone = function(el) {
                return {
                    name: el.name + " cloned"
                };
            }
            const log = function(evt) {
                window.console.log(evt);
            }
            const openEditDashboard = (id) => {

                console.log(id);
            }

            const modalEditTasksModule = reactive({
                isOpened: false,
                toggleOpened: boolean => modalEditTasksModule.isOpened = boolean,
            })

            return {
                clone,
                log,
                boards: computed(() => boards.data),
                openEditDashboard,
                modalEditTasksModule,
            }
        },
    };
</script>

<style lang="scss">
    .tasks {
        width: 100%;
        height: 100%;
        padding: 30px;
    }
    .tasks__row {
        width: 100%;
        height: 100%;
        display: flex;

    }
    .tasks__column {
        width: 300px;
        height: 100%;
        margin-right: 40px;
        padding: 15px;
        &:last-of-type {
            margin: 0;
        }
        background: #454545;
        box-shadow: 0px 4px 0px #454545;
        transition: .2s ease;
        border-radius: 12px;
        &:hover {
            box-shadow: 0px 4px 0px #FFD15C;
        }

    }
    .tasks__board-name {
        font-style: normal;
        font-weight: 500;
        font-size: 24px;
        line-height: 33px;

        color: #FFFFFF;
        text-align: left;
        margin: 5px 0;
        width: 100%;

        display: flex;
        justify-content: space-between;
    }
    .tasks__item {
        background: #E5F5FA;
        border-radius: 12px;
        padding: 20px 25px;
        margin: 15px 0;
        text-align: left;
        cursor: pointer;

        &.tasks__item_create {
            font-style: normal;
            font-weight: bold;
            font-size: 18px;
            line-height: 25px;
            color: white;

            text-align: center;
            background: #454545;
            border: 2px dotted white;
        }
    }

</style>