### 5.1 Cannot Set LC_ALL to Default Locale

If running the locale command results in the error message

`locale: Cannot set LC_ALL to default locale: No such file or directory`

then the support for the particular language has not been installed. To install it, run the command (example uses the English language):

`sudo apt install language-pack-en`

Then, to update the system’s locale files, run the following commands (this example uses the US locale):

`sudo locale-gen en_US.UTF-8`<br>
`sudo update-locale en_US.UTF-8`

Set the operating system locale. Add following line to /etc/environment file.

`LC_ALL=en_US.UTF-8`

After updating the system’s locale settings, it is recommended to restart the operating system.