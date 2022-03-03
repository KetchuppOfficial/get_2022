##Создание SSH ключа
* Ввести в терминале команду
```
ssh-keygen -t ed25519 -C "example_email@domen.com"
```

* Далее появится сообщение, свидетествующиее о создании SSH ключа
```
> Generating public/privat ed 25519 key pair
```

* Затем необходимо ввести название файла, в котором будет сохранён SSH ключ (или можно ввести Enter, в результате чего расположение файла будет стандартным
```
> Enter a file in which to save the key (/Users/you/.ssh/id_ed25519)
```

* Также появится возможность добавить пароль (лучше это не делать)
```
> Enter passphrase (empty for no passphrase): [Press enter]
> Enter same passphrase again: [Press enter]
```


