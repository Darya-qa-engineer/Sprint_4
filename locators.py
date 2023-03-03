from selenium.webdriver.common.by import By


class Locators:
    # Кнопка принять куки
    COOKIE_BTN = [By.XPATH, '//button[@id="rcc-confirm-button"]']

    # Кнопка "Заказать" в углу страницы
    ORDER_BTN_TOP_RIGHT = [By.XPATH,
                           '//div[starts-with(@class, "Header_Header")]//button[contains(text(), "Заказать")]']

    # Кнопка "Заказать" внизу страницы
    ORDER_BTN_DOWN = [By.XPATH, '//div[starts-with(@class, "Home_FinishButton")]//button[contains(text(), "Заказать")]']

    # Форма регистрации
    # Поле "Имя" при оформлении заказа
    ORDER_FORM_NAME_FIELD = [By.XPATH, '//div[starts-with(@class, "Order_Form")]//input[@placeholder="* Имя"]']

    # Поле "Фамилия" при оформлении заказа
    ORDER_FORM_LAST_NAME_FIELD = [By.XPATH, '//div[starts-with(@class, "Order_Form")]//input[@placeholder="* Фамилия"]']

    # Поле "Адрес" при оформлении заказа
    ORDER_FORM_ADDRESS_FIELD = [By.XPATH,
                                '//div[starts-with(@class, "Order_Form")]//input[@placeholder="* Адрес: куда привезти заказ"]']

    # Поле "Станция метро" при оформлении заказа
    ORDER_FORM_METRO_FIELD = [By.XPATH,
                              '//div[starts-with(@class, "Order_Form")]//input[@placeholder="* Станция метро"]']

    # Выбраная станция метро при оформлении заказа
    ORDER_FORM_METRO_NAME = [By.XPATH,
                             '//li[starts-with(@class, "select-search__row")]//button[@class = "Order_SelectOption__82bhS"]']

    # Инпут периода аренды формы заказа
    ORDER_FORM_DATE_RENTAL_PERIOD_INPUT = [By.XPATH, './/div[contains(@class, "Dropdown-root")]']

    # Результаты поиска станции метро
    METRO_SEARCH_RESULTS = [By.XPATH, '//li[@class="select-search__row"]']

    # Поле "Телефон" при оформлении заказа
    ORDER_FORM_PHONE_FIELD = [By.XPATH,
                              '//div[starts-with(@class, "Order_Form")]//input[@placeholder="* Телефон: на него позвонит курьер"]']

    # Календарь
    ORDER_FORM_DELIVERY_DATE_INPUT = [By.XPATH,
                                      '//div[@class="react-datepicker__input-container"]//input[@placeholder="* Когда привезти самокат"]']

    # Кнопка "Заказать" формы заказа
    ORDER_FORM_MAKE_ORDER_BTN = [By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]']

    # Кнопка "Далее" при заказе
    ORDER_FORM_BTN_NEXT = [By.XPATH, '//div[starts-with(@class, "Order_NextButton")]//button']

    # Date picker локаторы
    DATE_PICKER = [By.XPATH, '//div[@class="react-datepicker"]']
    # Сетка дней дейтпикера
    DATE_PICKER_GRID = [By.XPATH, './/div[@class="react-datepicker__month"]']
    # День в сетке дейтпикера
    DATE_PICKER_DAY = [By.XPATH, './/div[contains(@class, "react-datepicker__day")]']
    # Селектор дня в сетке дейтпикера по номеру дня
    DATE_PICKER_SPECIFIC_DAY = lambda day: [By.XPATH,
                                            f'.//div[contains(@class, "react-datepicker__day") and text()="{day}"]']
    # Выбранный день в сетке дейтпикера
    DATE_PICKER_SELECTED_DAY = [By.XPATH, './/div[contains(@class, "selected")]']
    # "Сегодня" в сетке дейтпикера
    DATE_PICKER_TODAY = [By.XPATH, './/div[contains(@class, "react-datepicker__day--today")]']
    # Последний день в сетке дейтпикера
    DATE_PICKER_LAST_DAY = [By.XPATH, './/div[@class="react-datepicker__week"][last()]/div[last()]']
    # Первый день в сетке дейтпикера
    DATE_PICKER_FIRST_DAY = [By.XPATH, './/div[@class="react-datepicker__week"][1]/div[1]']
    # Кнопка "Следующий месяц" в дейтпикере
    DATE_PICKER_NEXT_BTN = [By.XPATH, './/button[contains(@class, "react-datepicker__navigation--next")]']
    # Текущий месяц дейтпикерп
    DATE_PICKER_CURRENT_MONTH = [By.XPATH, './/div[@class="react-datepicker__current-month"]']

    # Меню дропдаун компонента
    DROPDOWN_MENU = [By.XPATH, '//div[@class="Dropdown-menu"]']
    # Опция дропдауна по тексту
    DROPDOWN_OPTION_BY_VALUE = lambda val: [By.XPATH, f'.//div[@class="Dropdown-option" and text()="{val}"]']

    # Плейсхолдер дропдауна
    DROPDOWN_INPUT_PLACEHOLDER = [By.XPATH, './/div[contains(@class, "Dropdown-placeholder")]']

    # Модальное окно на странице заказа
    ORDER_MODAL = [By.XPATH, '//div[contains(@class, "Order_Modal")]']
    # Хидер модального окна на странице заказа
    ORDER_MODAL_HEADER = [By.XPATH, '//div[contains(@class, "Order_ModalHeader")]']
    # Кнопка "да" в модальном окне страницы заказа
    ORDER_MODAL_YES_BTN = [By.XPATH, './/button[contains(text(), "Да")]']
    # Кнопка "посмотреть статус" в модальном окне страницыц заказа
    ORDER_MODAL_VIEW_BTN = [By.XPATH, './/button[contains(text(), "Посмотреть статус")]']
    # Текст модального окна страницы заказа
    ORDER_MODAL_TEXT_CONTAINER = [By.XPATH, './/div[contains(@class, "Order_Text")]']

    # Форма трекинга
    TRACK_FORM = [By.XPATH, '//div[contains(@class, "Track_Form")]']
    # Инпут номера заказа
    TRACK_FORM_INPUT = [By.XPATH, '//div[contains(@class, "Track_Form")]//input']
    # Селектор информации заказа на странице трекинга
    TRACK_ORDER_INFO = [By.XPATH, '//div[contains(@class, "Track_OrderInfo")]']
    # Строка инфы заказа на странице трекинга
    TRACK_ORDER_ROW = [By.XPATH, './/div[contains(@class, "Track_Row")]']
    # Имя значения в инфе заказа на странице трекинга
    TRACK_ORDER_ROW_TITLE = [By.XPATH, './/div[contains(@class, "Track_Title")]']
    # Ячейка имени инфы заказа по тексту
    TRACK_ORDER_ROW_TITLE_BY_TEXT = lambda txt: [By.XPATH,
                                                 f'.//div[contains(@class, "Track_Title") and text()="{txt}"]']
    # Ячейка значения инфы заказа
    TRACK_ORDER_ROW_VALUE = [By.XPATH, './/div[contains(@class, "Track_Value")]']
    # Ячейка значения инфы заказа по имени
    TRACK_ORDER_ROW_VALUE_FOR_TITLE = lambda txt: [By.XPATH,
                                                   f'.//div[contains(@class, "Track_Title") and text()="{txt}"]/following-sibling::div']
    # Роадмап статусов заказа
    TRACK_ORDER_ROADMAP = [By.XPATH, './/div[contains(@class, "Track_OrderRoadmap")]']
    # Крипичик роадмапа статусов заказа
    TRACK_ORDER_ROADMAP_BRICK = [By.XPATH, './/div[contains(@class, "Track_OrderBrick")]']
    # Подсвеченный кирпичик роадмапа статусов заказа
    TRACK_ORDER_ROADMAP_BRICK_HIGHLIGHTED = [By.XPATH, './/div[contains(@class, "Track_Highlight")]']
    # Имя ккрипичика роадмапа статусов заказов
    TRACK_ORDER_ROADMAP_BRICK_TITLE = [By.XPATH,
                                       './/div[contains(@class, "Track_OrderInfo")]//div[contains(@class, "Track_Order")]']
    # Элемент компонента "Аккордион"
    ACCORDION_ITEM = [By.XPATH, './/div[@class="accordion__item"]']
    # Заголовок элемента компонента "Аккордион"
    ACCORDION_ITEM_HEADING = [By.XPATH, './/div[@class="accordion__button"]']
    #  Значение элемента компонента "Аккордион"
    ACCORDION_ITEM_PANEL = [By.XPATH, './/div[@class="accordion__panel"]']

    # Блок вопросов
    HOME_FAQ_CONTAINER = [By.XPATH, '//div[starts-with(@class, "Home_FAQ")]']

    # Логотип Яндекс
    YANDEX_LOGO = [By.XPATH, '//div[contains(@class,"Header_Logo")]//a[@href="//yandex.ru"]']

    # Логотип Самоката
    SCOOTER_LOGO = [By.XPATH, '//div[contains(@class,"Header_Logo")]//a[@href="/"]']
    # Я устала :(
