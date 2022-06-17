## How to set up the environvent to run the frontend

Follow this guide 'Setting up the development environment' for React Native:

https://reactnative.dev/docs/environment-setup

Ignore the 'Creating a new application' section, that has already been done. Instead, using a terminal emulator, in the 'frontend' directory, run 
```
npm install
```

The other steps in the guide need to be performed to get the enviroment working.

## How to run (emulate) the frontend (for Linux)
These steps are also in the guide above, for all operating systems. The following will be specific for Linux, for emulating the app on Android, but the commands are similar if not identical on other operating systems.

You need to have set up the environment according to the section above for the following to work.

In a terminal emulator window, go to the 'frontend' directory and run
```
npx react-native start
```
Keep this window open.

In another terminal emulator window, go to the 'frontend' directory and run
```
npx react-native run-android
```
