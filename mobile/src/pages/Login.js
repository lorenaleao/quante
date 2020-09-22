import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet, Alert} from 'react-native';

import api from '../services/api';

function Login({navigation}){

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    async function submitLogin() {
        const response = await api.get('/login/login/'+email+'/'+password,).then((response) => {
            if (response.status === 200) {
                Alert.alert(
                    "Sucesso!",
                    "Login realizado com sucesso!",
                    [
                    { text: "OK", onPress: () => navigation.navigate('Quanté?') }
                    ]
                )
                setEmail('')
                setPassword('')
            }
        })
    }

    return(
        <View style={{flex:1}}>
            <Text style={styles.loginLabel}>Login:</Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.loginForm}>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o seu email"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={email}
                onChangeText={setEmail}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira sua senha"
                placeholderTextColor="#999"
                secureTextEntry={true}
                autoCorrect={false}
                value={password}
                onChangeText={setPassword}
                />
                <View style={{ height: 10 }}></View>
                <View style={{ height: 40 }}></View>
                <Button
                style = {styles.submitButton}
                onPress={submitLogin}
                title="Login"
                color="#1e5bc6"
                />
            </View>
        </View>
    );

}

const styles = StyleSheet.create({
    defaultTextInput: {
        padding: 8,
        backgroundColor: '#FFF'
    },
    loginLabel: {
        marginTop: 20,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
    },
    submitButton: {
        marginLeft: 20,
        marginRight: 20,
    },
    loginForm: {
        flex: 1,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
        flexDirection: 'column',
    }
});

export default Login;