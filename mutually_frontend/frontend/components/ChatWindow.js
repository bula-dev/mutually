import React, { useState } from 'react';
import {ScrollView, StyleSheet, Text, View, TextInput} from 'react-native';

const Button = ({children, design}) => {
  return (
    <View style={design}>
      <Text style={{color: 'white', fontSize: 20}}>{children}</Text>
    </View>
  );
};

const ChatWindow = () => {
  const [messageText, setMessageText] = useState("");

  return (
    <View style={styles.container}>
      <ScrollView style={{maxHeight: '95%'}}></ScrollView>

      <View style={styles.textBoxContainer}>
        {/* <Text style={styles.temp}>Message here</Text> */}

        <TextInput
          multiline
          placeholder='Write your message here'
          // numberOfLines={4}
          onChangeText={text => setMessageText(text)}
          value={messageText}
          style={styles.textBox}
        />

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

  textBox: {
    backgroundColor: "white",
    width: "80%",
    borderRadius: 5,
    maxHeight: 100
  },

  textBoxContainer: {
    backgroundColor: 'blue',
    padding: 10,
    // minHeight: 10,
    flexDirection: 'row',
  },

  sendButton: {
    backgroundColor: 'green',
    padding: 5,
    margin: 5,
    marginTop: 0,
    marginBottom: 0,
    borderRadius: 5,
    height: 40,
  },
});

export default ChatWindow;
