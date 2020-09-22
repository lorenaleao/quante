import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet} from 'react-native';
function CadastraEstabelecimento(){

    const [establishmentName, setEstablishmentName] = useState('');

    function submitNewEstablishment() {
        //const response = await api.post('', {params: {establishmentName}})
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