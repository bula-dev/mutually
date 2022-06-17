import React from 'react';
import {ScrollView, StyleSheet, Text, View, TextInput} from 'react-native';

const Button = ({children, design}) => {
  return (
    <View style={design}>
      <Text style={{color: 'white', fontSize: 20}}>{children}</Text>
    </View>
  );
};

const ChatWindow = () => {
  return (
    <View style={styles.container}>
      <ScrollView style={{maxHeight: '90%'}}></ScrollView>

      <View style={styles.textBoxContainer}>
        <Text style={styles.temp}>Message here</Text>
        {/* <TextInput multiline numberOfLines={4} onChangeText={text => setMessageText(text)} value={messageText} /> */}
          
        <Button design={styles.sendButton}>Send</Button>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    height: '100%',
    backgroundColor: 'white',
  },

  message: {},

  textBox: {},

  textBoxContainer: {
    backgroundColor: 'blue',
    padding: 10,
    minHeight: 100,
    flexDirection: "row"
  },

  sendButton: {
    backgroundColor: 'green',
    padding: 5,
    margin: 5,
    borderRadius: 5
  },

  temp: {
    backgroundColor: 'white',
    color: 'black',
  },
});

export default ChatWindow;
