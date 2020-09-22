import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet} from 'react-native';
function CadastraUsuario(){

    const [name, setName] = useState('')
    const [lastName, setLastName] = useState('')
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    function submitNewUser() {
        //const response = await api.post('', {params: {name, lastName, email, password}})
    }

    return(
        <View style={{flex:1}}>
            <Text style={styles.loginLabel}>Cadastre-se: </Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.loginForm}>
                <TextInput 
                placeholder="Insira o seu nome"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={name}
                onChangeText={setName}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                placeholder="Insira o seu sobrenome"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={lastName}
                onChangeText={setLastName}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                placeholder="Insira o seu email"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={email}
                onChangeText={setEmail}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                placeholder="Insira sua senha"
                placeholderTextColor="#999"
                autoCapitalize="words"
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