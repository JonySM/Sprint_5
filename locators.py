from selenium.webdriver.common.by import By


class Locators:
    LOGIN_INPUT_FIELD = (By.XPATH, ".//input[@name='name']")  # Ввод логина(почта)
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # Ввод пароля
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка войти в аккаунт
    LOGIN_MAIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка войти с главной страницы(формы)
    MAIN_TEXT = (By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']")  # Текст "Собери бургер"
    OUR_NAME_TEXT = (By.XPATH, ".//input[@value='Джони']")  # Отображение нашего имени
    OUR_LOGIN_TEXT = (By.XPATH, ".//input[@value='jony@yandex.ru']")  # Отображение нашего логина
    L_K_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Переход в ЛК
    CONSTRUCTOR_BUTTON =(By.XPATH, ".//p[text()='Конструктор']")  # Переход в конструктор
    LOGOUT_BUTTON_INSIDE_LK = (By.XPATH, ".//button[text()='Выход']")  # Кнопка выхода из ЛК
    REGISTRATION_BUTTON = (By.XPATH, ".//a[starts-with(@href, '/register')]")  # Кнопка зарегистрироваться
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//a[starts-with(@href, '/forgot-password')]")  # Кнопка восстановить пароль
    LOGIN_OPTIONAL_BUTTON = (By.XPATH, ".//a[starts-with(@href, '/login')]")  # Кнопка войти со страницы регистрации/востановления
    CONSTRUCTOR_BUNS = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() ='Булки']")  # Раздел конструктора булки
    CONSTRUCTOR_SAUCES = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() ='Соусы']")  # Раздел конструктора соусы
    CONSTRUCTOR_TOPPINGS = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() ='Начинки']")  # Раздел конструктора начинки
    STEP_ON_THE_TAB = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  # Переход на вкладку
    REGISTRATION_NAME_FILD = (By.NAME, "name")  # Имя в форме регистрации
    REGISTRATION_EMAIL_FILD = (By.XPATH, ".//label[text()='Email']/parent::*/input")  # Почта в форме регистрации
    REGISTRATION_PASSWORD_FILD = (By.NAME, "Пароль")  # Пароль в форме регистрации
    REGISTRATION_MAIN_BUTTON = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")  # Кнопка зарегистроваться(на форме регистрации)
    MAIN_LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")  # Текст "Вход" над формой для входа
    ERROR_TEXT = (By.XPATH, ".//p[@class='input__error text_type_main-default']")  # Текст ошибки регистрации





