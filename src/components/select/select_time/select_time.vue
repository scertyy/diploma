<template>
    <div class="start_specialty_time time" id="sdfljkshdf" @focus="showSelect" @blur="hideSelect" tabindex="0">
        <div class="start_specialty__title select_time" :class="{ 'selected' : isSelected }" id="time_form">
            <p id="isValueTime" class="current_value">{{ defaultValue }}</p>
            <div class="btn-if">
                <button @click="showSelect" class="select_open">
                    <svg width="14" height="8" viewBox="0 0 14 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M6.98805 7.98682L7.00069 8L14 0.695993L13.3334 0.00034851L7.00037 6.60904L0.666621 -0.000436995L-3.17609e-06 0.695208L6.98773 7.98715L6.98805 7.98682Z"/>
                    </svg>
                </button>
                <button @click="select_reset" class="select_reset">
                    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M0 0.666708L0.666647 4.38888e-05L13.9996 13.3333L13.3329 14L0 0.666708Z"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M13.3334 0L14 0.666664L0.667064 14L0.000417038 13.3333L13.3334 0Z"/>
                    </svg>
                </button>
            </div>
        </div>
        <transition name="bounce">
            <div class="start_specialty__list-wrapper" v-if="isActive">
                <ul class="start_specialty__list" style="display: grid; grid-template-columns: 1fr 1fr 1fr; width: 100%;">
                    <li @click="setValue" v-for="(item, index) in times" :id="'time_' + index" :key="24 * 5" style="white-space: nowrap; ">
                        {{ item.service }}
                    </li>
                </ul>
            </div>
        </transition>
    </div>
</template>

<script src="./select_time.js"></script>