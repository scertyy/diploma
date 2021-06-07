<template>
    <div class="auth">
        <div class="auth__body" v-if="selectedReg">
            <h1 class="auth__h1">Регистрация</h1>
            <div class="auth__input-group">
                <BaseInput class="base-input_mb-30"
                           placeholder="Логин"
                           v-model="registerData.username"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Электронная почта"
                           v-model="registerData.email"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Номер телефона"
                           v-model="registerData.phone"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Пароль"
                           v-model="registerData.password"
                ></BaseInput>
                <BaseInput placeholder="Повторите пароль"
                           v-model="registerData.repeatPassword"
                ></BaseInput>
            </div>
            <div class="auth__buttons-cont">
                <BaseButton>Зарегистрироваться</BaseButton>
            </div>
        </div>
        <div class="auth__body" v-else>
            <h1 class="auth__h1">Авторизация</h1>
            <div class="auth__input-group">
                <BaseInput class="base-input_mb-30"
                           placeholder="Логин"
                           v-model="registerData.username"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Пароль"
                           v-model="registerData.password"
                ></BaseInput>
            </div>
            <div class="auth__buttons-cont">
                <BaseButton>Войти</BaseButton>
            </div>
        </div>
    </div>
</template>

<script>
    import {reactive, ref} from 'vue'
    import BaseButton from '../../components/BaseButton'
    import BaseInput from '../../components/BaseInput'
    export default {
        components: {
            BaseButton,
            BaseInput,
        },
        setup() {
            const loginData = reactive({
                username: '',
                password: '',
            })
            const registerData = reactive({
                username: '',
                email: '',
                phone: '',
                password: '',
                repeatPassword: '',
            })
            const selectedReg = ref(false);
            return {
                loginData,
                registerData,
                selectedReg,
            }
        }
    }
</script>

<style lang="scss">
    .auth {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .auth__body {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .auth__input-group {
        display: flex;
        flex-direction: column;
    }
    .auth__buttons-cont {
        display: flex;

        margin-top: 50px;
    }
</style>