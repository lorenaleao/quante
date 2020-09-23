import React, { useState, useEffect } from 'react';
import {View, Text, TextInput, Button, StyleSheet, Picker, Alert} from 'react-native';

import api from '../services/api';

function AtualizaPrecoProduto() {

    const [newPrice, setNewPrice] = useState('');

    async function atualizaPreco() {
        const response = await api.get('/product/update_price/5f6aab6236cb42f490b1578d/5f6aabe7f9ec3d3194677ac1/'+newPrice).then((response) => {
            Alert.alert("Sucesso!", "Requisição de mudança de preço enviada com sucesso!")
        })
    }

    return(
        <View style={{flex:1}}>
            <View style={{ height: 10 }}></View>
            <View style={styles.newProductForm}>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o novo preço para o produto"
                placeholderTextColor="#999"
                keyboardType="numeric"
                autoCorrect={false}
                value={newPrice}
                onChangeText={setNewPrice}
                />
                <View style={{ height: 10 }}></View>
                <View style={{ height: 40 }}></View>
                <Button
                style = {styles.submitButton}
                onPress={atualizaPreco}
                title="Atualizar preço"
                color="#1e5bc6"
                />
            </View>
        </View>
    );

}

const styles = StyleSheet.create({
    defaultTextInput: {
        marginLeft: 20,
        marginRight: 20,
        padding: 8,
        backgroundColor: '#FFF'
    },
    submitButton: {
        marginLeft: 20,
        marginRight: 20,
    },
    newProductForm: {
        flex: 1,
        zIndex: 5,
        flexDirection: 'column',
    }
});

export default AtualizaPrecoProduto;