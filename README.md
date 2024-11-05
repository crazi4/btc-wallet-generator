# btc-wallet-generator

##Скрипт, который генерирует Bitcoin кошельки используя случайно сгенерированные seed-фразы

###1. Метод работы

Библиотека Mnemonic случайным образом генерирует слова, из которых получается seed-фраза, которая является кошельком в незашифрованном виде.
Дальше, идёт поэтапное шифрование, в результате чего мы получаем WIF (Wallet important format), то есть адрес кошелька в блокчейне, а так же приватный и публичный ключи.
С использованием API отправляем запрос в любой блокчейн, API которого вы обладаете (API должен быть обязательно ваш), и если транзакции на кошельке нашлись, значит кошелёк действующий, а значит потенциально может иметь крипту на кошельке.
Если транзакций нет, значит кошелёк или пустой, или его не существует вовсе.

###2. Как получить API?

Чтобы получить API, нужно найти интересующий вас блокчейн (99% API платные, и имеют ограничения по запросам).

###3. Библиотеки, которые нужны для работы скрипта

mnemonic
bitcoin
bitcoinlib (bitcoinlib.keys)
requests
json
###4. Контакты для обратной связи
Telegram: https://t.me/crazi444
Пишите, если есть какие-то вопросы или претензии по работе скрипта.
