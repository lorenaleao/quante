import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet, Alert} from 'react-native';

import api from '../services/api';

function CadastraEstabelecimento({navigation}){

    const [establishmentName, setEstablishmentName] = useState('');
    const [cnpj, setCnpj] = useState('');
    const [address, setAdress] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    async function submitNewEstablishment() {
        let today = new Date()
        let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
        let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()
        let dateTime = date+' '+time
        const response = await api.post('/company/post/', {
            name: establishmentName,
            cnpj,
            address,
            email,
            password,
            create_date: dateTime
        }).then((response) => {
            Alert.alert(
                "Sucesso!",
                "Estabelecimento cadastrado com sucesso!",
                [
                { text: "OK", onPress: () => navigation.navigate('Quanté?') }
                ]
            )
            setEstablishmentName('')
            setCnpj('')
            setAdress('')
            setEmail('')
            setPassword('')
        })
    }

    return(
        <View style={{flex:1}}>
            <Text style={styles.newEstablishmentLabel}>Cadastre um estabelecimento:</Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.newEstablishmentForm}>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o nome do estabelecimento"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={establishmentName}
                onChangeText={setEstablishmentName}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o CNPJ do estabelecimento"
                placeholderTextColor="#999"
                autoCorrect={false}
                value={cnpj}
                onChangeText={setCnpj}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o endereço do estabelecimento"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={address}
                onChangeText={setAdress}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o email do estabelecimento"
                placeholderTextColor="#999"
                autoCorrect={false}
                value={email}
                onChangeText={setEmail}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira a senha do estabelecimento"
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
                onPress={submitNewEstablishment}
                title="Adicionar estabelecimento"
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
    newEstablishmentLabel: {
        marginTop: 20,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
    },
    submitButton: {
        marginLeft: 20,
        marginRight: 20,
    },
    newEstablishmentForm: {
        flex: 1,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
        flexDirection: 'column',
    }
});

export default CadastraEstabelecimento;