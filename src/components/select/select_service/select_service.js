export default {
    name: "select_service",
    components: {},
    data() {
        return {
            isActive: false,
            transition: 100,
            isDrop: true,
            isSelected: false,
            defaultValue: 'Выберите специальность',
            id_item: '',
            counter: false,
            items: [
                {
                    service: 'Гастроэнтерология'
                },
                {
                    service: 'Гинекология'
                },
                {
                    service: 'Кардиология'
                },
                {
                    service: 'Лабороторная диагностика'
                },
                {
                    service: 'Неврология'
                },
                {
                    service: 'Процедуры'
                },
                {
                    service: 'Пульмонология'
                },
                {
                    service: 'Терапия'
                },
                {
                    service: 'Ультрозвуковая диагностика (УЗИ)'
                },
                {
                    service: 'Экспертиза временной нетрудоспособности'
                },
                {
                    service: 'Электрокардиография (ЭКГ)'
                },
                {
                    service: 'Эндокринология'
                },
            ]
        }
    },
    methods: {
        hideSelect() {
            let currentActive = false;
            this.isActive = currentActive;

            setTimeout(function () {
                this.isActive = currentActive;
            },)
        },
        select_reset() {
            let defaultValue = this.defaultValue;
            let currentSelect = document.querySelectorAll('#isValue');
            for (let i = 0; i < currentSelect.length; i++) {
                currentSelect[i].style.transition = this.transition / 1000 + 's';
                currentSelect[i].style.opacity = 0;
                currentSelect[i].style.transform = 'translateY(-10px)';
                setTimeout(function () {
                    currentSelect[i].style.transform = 'translateY(0)';
                    currentSelect[i].style.opacity = 1;
                    currentSelect[i].style.color = 'rgba(35, 35, 35, 0.5)';
                    currentSelect[i].innerText = defaultValue;
                }, this.transition)
            }

            this.hideSelect();
            this.isDrop = true;
            this.isSelected = false;
            if (this.isSelected === false) {
                this.counter = true;
            }

            let buttons = document.querySelectorAll('.select_service')
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].classList.remove('selected');
            }
        },
        setValue() {
            let selected;
            const handleClick = event => {
                const id = event.target.id;
                this.id_item = document.getElementById(id).getAttribute('id');

                selected = document.getElementById(id).textContent;
                let buttons = document.querySelectorAll('#isValue')
                console.log(selected)
                for (let i = 0; i < buttons.length; i++) {
                    document.querySelectorAll('#isValue')[i].textContent = selected;
                }
            }
            let currentSelect = document.querySelectorAll('#isValue');
            for (let i = 0; i < currentSelect.length; i++) {
                currentSelect[i].style.transition = this.transition / 1000 + 's';
                currentSelect[i].style.opacity = 0;
                currentSelect[i].style.transform = 'translateY(-10px)';
                currentSelect[i].style.transition = this.transition / 1000 + 's';
                setTimeout(function () {
                    currentSelect[i].innerText = selected;
                    currentSelect[i].style.color = '#232323'
                    currentSelect[i].style.opacity = 1;
                    currentSelect[i].style.transform = 'translateY(0px)';
                }, this.transition);
            }
            this.isSelected = true;


            document.querySelector(".start_specialty__list").addEventListener("click", handleClick);
            this.hideSelect();
            let selector = document.querySelectorAll('.start_specialty_item')
            for (let i = 0; i < selector.length; i++) {
                selector[i].blur();
            }

            this.isDrop = false;
            this.isSelected = false;
            if (this.isSelected === false) {
                this.counter = false;
            }


            let buttons = document.querySelectorAll('.select_service')
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].classList.add('selected');
            }
        },
        showSelect() {
            setTimeout(function () {
                if (document.querySelectorAll('.start_specialty__list li').length > 5) {
                    document.querySelectorAll('.start_specialty__list li').forEach(e => e.style.marginRight = '10px');
                }
            });
            this.isActive = true;
            let id_service = this.id_item;

            if (this.counter != true) {
                setTimeout(function () {
                    if (id_service) {
                        document.getElementById(id_service).classList.add('active');
                        document.getElementById(id_service).style.pointerEvents = 'none';
                    }
                },)
            } else {
                setTimeout(function () {
                    if (id_service) {
                        document.getElementById(id_service).classList.remove('active');
                        document.getElementById(id_service).style.pointerEvents = 'auto';
                    }

                },)
            }
        },
    },
}