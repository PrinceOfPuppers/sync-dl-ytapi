<img align="left" width="80" height="80" src="https://raw.githubusercontent.com/PrinceOfPuppers/sync-dl/main/icon.png">

# sync-dl-ytapi
<p>
<img src="https://img.shields.io/pypi/dm/sync-dl-ytapi">
<img src="https://img.shields.io/pypi/l/sync-dl-ytapi">
<img src="https://img.shields.io/pypi/v/sync-dl-ytapi">
<img src="https://img.shields.io/badge/python-%E2%89%A53.6-blue">

</p>


> An addon for sync-dl, providing commands which utilize the youtube api
- [INSTALLATION](#INSTALLATION)
- [ABOUT](#ABOUT)
- [USAGE](#USAGE)
- [EXAMPLE](#EXAMPLE)
- [DEVLOPMENT](#DEVLOPMENT)

# INSTALLATION
First install sync-dl:
```
pip install sync-dl
```
Using any commands in sync-dl which require this addon will prompt the user to install this addon.


# ABOUT
Provides the --push-order option to sync-dl (along with potentially more in the future)


# Usage
```
sync-dl ytapi --push-order PLAYLIST
```
This will prompt you to install sync-dl-ytapi if you have not already, and will
print out the url to log in with google. Once you have done this it will
push the local order of PLAYLIST to youtube, reordering songs to match the local order (songs in remote but not in local will always stay after what they are currently after)

PLAYLIST is simply the name of the directory which contains the playlist. playlist directory will always be in current working directory unless a music directory is specified using the -l, --local-dir option to hard set a music directory.

You can also logout (revoke the access tokens and delete the saved credentials) using
the following command
```
sync-dl ytapi --logout
```

To see all options use the command:
```
sync-dl ytapi -h
```

## Transfer Command:
```
sync-dl ytapi transfer [OPTINOS] SRC_PLAYLIST DEST_PLAYLIST
```
Transfers songs between `SRC_PLAYLIST` and `DEST_PLAYLIST` on both local and remote, moving a single song using `-t SI DI` or a range of songs `-r S1 S2 DI`

To see all options as well as a more indepth description use the command:
```
sync-dl ytapi transfer -h
```

# DEVLOPMENT
To build for devlopment run:
```
git clone https://github.com/PrinceOfPuppers/sync-dl-ytapi.git

cd sync-dl-ytapi

pip install -e .
```
This will build and install sync-dl in place, allowing you to work on the code without having to reinstall after changes, it will also install sync-dl as it is a dependancy
