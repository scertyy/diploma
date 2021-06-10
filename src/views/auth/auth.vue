<template>
    <div class="auth">
        <div class="auth__body" v-if="selectedReg">
            <h1 class="auth__h1">Регистрация</h1>
            <div class="auth__input-group">
                <BaseInput class="base-input_mb-30"
                           placeholder="Имя"
                           v-model="registerData.last_name"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Фамилия"
                           v-model="registerData.first_name"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Логин"
                           v-model="registerData.username"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Электронная почта"
                           v-model="registerData.email"
                ></BaseInput>
                <BaseInput class="base-input_mb-30"
                           placeholder="Пароль"
                           v-model="registerData.password"
                           type="password"
                ></BaseInput>
            </div>
            <div class="auth__buttons-cont">
                <BaseButton class="base-button_w-100" @click="tryRegL">Зарегистрироваться</BaseButton>
            </div>
            <div class="auth__switch"><span  @click="selectedReg = false">У меня есть аккаунт</span></div>
        </div>
        <div class="auth__body" v-else>
            <h1 class="auth__h1">Авторизация</h1>

            <div class="auth__input-group">
                <BaseInput class="base-input_mb-30"
                           placeholder="Логин"
                           v-model="loginData.username"
                ></BaseInput>
                <BaseInput
                           placeholder="Пароль"
                           v-model="loginData.password"
                           type="password"
                ></BaseInput>
            </div>
            <div class="auth__success-message" v-if="successMessage">
                Регистрация прошла успешно. Авторизуйтесь.
            </div>
            <div class="auth__buttons-cont">
                <BaseButton class="base-button_w-100" @click="tryAuthL">Войти</BaseButton>
            </div>
            <div class="auth__switch"><span  @click="selectedReg = true">Зарегистрироваться</span></div>
        </div>
    </div>
</template>

<script>
    import {reactive, ref} from 'vue'
    import {useRouter} from 'vue-router'
    import BaseButton from '../../components/Base/BaseButton'
    import BaseInput from '../../components/Base/BaseInput'
    import {useAuth} from "../../composition/useAuth";
    export default {
        components: {
            BaseButton,
            BaseInput,
        },
        setup() {

            const { tryAuth, tryReg } = useAuth()
            const router = useRouter()

            const loginData = reactive({
                username: '',
                password: '',
            })
            const registerData = reactive({
                username: '',
                email: '',
                password: '',
                first_name: '',
                last_name: '',
            })

            const tryAuthL = () => {
                tryAuth({
                    username: loginData.username,
                    password: loginData.password
                })
                .then(r => {
                    if (r.access) {
                        localStorage.setItem('token_access', r.access);
                        router.push('/')
                    }
                })
            }
            const tryRegL = () => {
                tryReg({
                    username: registerData.username,
                    email: registerData.email,
                    password: registerData.password,
                    first_name: registerData.first_name,
                    last_name: registerData.last_name,
                })
                .then(r => {
                    if (r.success) {
                        selectedReg.value = false;
                        successMessage.value = true;
                    }
                })
            }
            const selectedReg = ref(false);
            const successMessage = ref(false);
            return {
                loginData,
                registerData,
                selectedReg,
                tryAuthL,
                tryRegL,
                successMessage,
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
        width: 500px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .auth__h1 {
        width: 100%;
        // font-family: PT Root UI;
        font-style: normal;
        font-weight: bold;
        font-size: 57px;
        line-height: 72px;
        /* identical to box height */

        text-align: center;

        color: #FFFFFF;
        text-align: center;
    }
    .auth__input-group {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .auth__buttons-cont {
        display: flex;
        width: 100%;

        margin-top: 30px;
        display: flex;
        justify-content: center;
    }
    .auth__switch {
        // font-family: PT Root UI;
        font-style: normal;
        font-weight: 500;
        font-size: 20px;
        line-height: 25px;
        text-align: left;
        color: #FFD15C;

        margin-top: 15px;
        span {
            cursor: pointer;
        }
    }
    .auth__success-message {
        margin: 30px 0 5px;
        // font-family: PT Root UI;
        font-style: normal;
        font-weight: normal;
        font-size: 22px;
        line-height: 115%;
        color: #4CCE59;
        text-align: left;
    }
</style>
