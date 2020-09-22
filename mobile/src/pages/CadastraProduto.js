import React, { useState } from 'react';
import {View, Text, TextInput, Button, StyleSheet} from 'react-native';
function CadastraProduto(){

    const [productName, setProductName] = useState('');
    const [productPrice, setProductPrice] = useState('');

    function submitNewProduct() {
        //const response = await api.post('', {params: {productName, productPrice...}})
    }

    return(
        <View style={{flex:1}}>
            <Text style={styles.newProductLabel}>Cadastre um produto:</Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.newProductForm}>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o nome do produto"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={productName}
                onChangeText={setProductName}
                />
                <View style={{ height: 10 }}></View>
                <TextInput 
                style={styles.defaultTextInput}
                placeholder="Insira o preço do produto"
                placeholderTextColor="#999"
                keyboardType="numeric"
                autoCorrect={false}
                value={productPrice}
                onChangeText={setProductPrice}
                />
                <View style={{ height: 40 }}></View>
                <Button
                style = {styles.submitButton}
                onPress={submitNewProduct}
                title="Adicionar produto"
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
    newProductLabel: {
        marginTop: 20,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
    },
    submitButton: {
        marginLeft: 20,
        marginRight: 20,
    },
    newProductForm: {
        flex: 1,
        marginLeft: 20,
        marginRight: 20,
        zIndex: 5,
        flexDirection: 'column',
    }
});

export default CadastraProduto;