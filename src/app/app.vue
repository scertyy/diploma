<template>
    <div class="main">
        <div class="modal_wrapper" style="z-index: 99999;">
            <modal_record id="modal_record"></modal_record>
            <div class="modal_background" id="modal_background" tabindex="0"></div>
        </div>
        <div class="background__dark" @click="hideBurger" tabindex="0"></div>
        <div class="modal-result-message-container">
            <div class="modal-result-message-wrapper">
                <div class="modal-result-message">
                    <div class="message-wrapper">
                        <p id="modal_message"></p>
                    </div>
                    <button class="close-modal">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                  d="M0 0.666708L0.666647 4.38888e-05L13.9996 13.3333L13.3329 14L0 0.666708Z"/>
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                  d="M13.3334 0L14 0.666664L0.667064 14L0.000417038 13.3333L13.3334 0Z"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <header_section></header_section>
        <div>
            <router-view></router-view>
        </div>
        <footer_section class="footer-bottom"></footer_section>
    </div>
</template>


<style src="./app.scss" lang="scss"></style>
<script src="./app.js"></script>
<style src="./layout/scss/style.scss" lang="scss"></style>
