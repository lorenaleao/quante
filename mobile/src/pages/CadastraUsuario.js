import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet, Alert} from 'react-native';

import api from '../services/api';

import Constants from "expo-constants";
const { manifest } = Constants;

function CadastraUsuario({navigation}){

    const [name, setName] = useState('')
    const [age, setAge] = useState('')
    const [cpf, setCpf] = useState('')
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    async function submitNewUser() {
        let today = new Date()
        let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
        let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()
        let dateTime = date+' '+time
        const response = await api.post('/client/post/', {
            name, 
            age: Number(age), 
            cpf, 
            email, 
            password, 
            create_date: dateTime
        }).then((response) => {
            Alert.alert(
                "Sucesso!",
                "Usuário cadastrado com sucesso!",
                [
                { text: "OK", onPress: () => navigation.navigate('Quanté?') }
                ]
            )
            setName('')
            setAge('')
            setCpf('')
            setEmail('')
            setPassword('')
        })
    }

    return(
        <View style={{flex:1}}>
            <Text style={styles.loginLabel}>Cadastre-se: </Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.loginForm}>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o seu nome"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={name}
                onChangeText={setName}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira sua idade"
                placeholderTextColor="#999"
                autoCorrect={false}
                value={age}
                onChangeText={setAge}
                keyboardType="numeric"
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira seu CPF"
                placeholderTextColor="#999"
                autoCorrect={false}
                value={cpf}
                onChangeText={setCpf}
                keyboardType="numeric"
                />
                <View style={{ height: 10 }}></View>
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
                onPress={submitNewUser}
                title="Cadastrar-se"
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

export default CadastraUsuario;