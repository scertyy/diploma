export default {
    name: "select_date",
    components: {},
    data() {
        return {
            isActive: false,
            transition: 100,
            isDrop: true,
            isSelected: false,
            defaultValue: 'Дата',
            id_item: '',
            counter: false,
            items: []
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
            let currentSelect = document.querySelectorAll('#isValueDate');
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


            let buttons = document.querySelectorAll('.select_date')
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].classList.remove('selected');
            }
        },
        setValue() {
            const handleClick = event => {
                const id = event.target.id
                this.id_item = document.getElementById(id).getAttribute('id');

                let selected = document.getElementById(id).textContent;
                let buttons = document.querySelectorAll('#isValueDate')
                console.log(selected)
                for (let i = 0; i < buttons.length; i++) {
                    document.querySelectorAll('#isValueDate')[i].textContent = selected;
                }
                let currentSelect = document.querySelectorAll('#isValueDate');
                for (let i = 0; i < currentSelect.length; i++) {
                    currentSelect[i].style.transition = this.transition / 1000 + 's';
                    currentSelect[i].style.opacity = 0;
                    currentSelect[i].style.transform = 'translateY(-10px)';
                    setTimeout(function () {
                        currentSelect[i].innerText = selected;
                        currentSelect[i].style.color = '#232323'
                        currentSelect[i].style.opacity = 1;
                        currentSelect[i].style.transform = 'translateY(0px)';
                    }, this.transition);
                    this.isSelected = true;
                }
            }
            document.querySelector(".start_specialty__list").addEventListener("click", handleClick);
            this.hideSelect();
            let selector = document.querySelectorAll('.start_specialty_date .date')
            for (let i = 0; i < selector.length; i++) {
                selector[i].blur();
            }
            this.isDrop = false;
            this.isSelected = false;
            if (this.isSelected === false) {
                this.counter = false;
            }

            let buttons = document.querySelectorAll('.select_date')
            for (let i = 0; i < buttons.length; i++) {
                buttons[i].classList.add('selected');
            }
        },
        showSelect() {


            setTimeout(function () {
                if (document.querySelectorAll('.start_specialty__list li').length > 9) {
                    document.querySelectorAll('.start_specialty__list').forEach(e => e.style.paddingRight = '10px');
                }
            });
            this.isActive = true;
            let id_service = this.id_item;


            function randomInteger(min, max) {
                let rand = min - 0.5 + Math.random() * (max - min + 1);
                return Math.round(rand);
            }

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
            setTimeout(function () {

                let dateCounter = document.querySelectorAll('.start_specialty__list li').length - 1;


                let randomCount1 = 'date_' + randomInteger(0, dateCounter);
                let randomCount2 = 'date_' + randomInteger(0, dateCounter);
                let randomCount3 = 'date_' + randomInteger(0, dateCounter);
                let randomCount4 = 'date_' + randomInteger(0, dateCounter);
                let randomCount5 = 'date_' + randomInteger(0, dateCounter);

                if (id_service != randomCount1) {
                    document.getElementById(randomCount1).classList.add('closed');
                }
                if (id_service != randomCount2) {
                    document.getElementById(randomCount2).classList.add('closed');
                }
                if (id_service != randomCount3) {
                    document.getElementById(randomCount3).classList.add('closed');
                }
                if (id_service != randomCount4) {
                    document.getElementById(randomCount4).classList.add('closed');
                }
                if (id_service != randomCount5) {
                    document.getElementById(randomCount5).classList.add('closed');
                }
            })
        },
    },
    mounted() {
        let dateNow = new Date();
        for (let i = 0; i < 9; i++) {
            let milliseconds = dateNow.setDate(dateNow.getDate() + 1);
            let currentDate = new Date(milliseconds);
            currentDate = currentDate.toISOString();
            currentDate = currentDate.split('T');
            currentDate = currentDate[0].split('-');
            currentDate = currentDate[2] + '.' + currentDate[1]
            this.items.push({service: currentDate});
        }
    }
}