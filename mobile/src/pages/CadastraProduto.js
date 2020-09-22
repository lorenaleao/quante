import React, { useState, useEffect } from 'react';
import {View, Text, TextInput, Button, StyleSheet, Picker} from 'react-native';

import api from '../services/api';

function CadastraProduto(){

    const [companies, setCompanies] = useState([]);
    const [selectedValue, setSelectedValue] = useState([]);

    const [productName, setProductName] = useState('');
    const [description, setDescription] = useState('');
    const [productPrice, setProductPrice] = useState('');

    async function submitNewProduct() {
        let companyId = selectedValue._id;
        let today = new Date()
        let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
        let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()
        let dateTime = date+' '+time
        const response = await api.post('/product/post/', {
            name: productName,
            image: null,
            description, 
            spec : {

            },
            categories: [],
            prices: {
                companyId: (productPrice, [1.0, 1.1, 1.0, 1.0])
            },
            price_history : [(dateTime, productPrice)],
            reviews : []

        })
    }

    useEffect(() => {
        api.get('/company/list/').then((response) => {
            setCompanies(response.data)
        })
    }, [])

    return(
        <View style={{flex:1}}>
            <Text style={styles.newProductLabel}>Cadastre um produto:</Text>
            <View style={{ height: 20 }}></View>
            <View style={styles.newProductForm}>
                <Picker
                    selectedValue={selectedValue}
                    style={{ height: 50, width: 150 }}
                    onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
                >
                    {companies.map(company => {
                        return <Picker.Item key={company._id} label={company.name} value={company.name} />
                    })}
                </Picker>
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
                placeholder="Insira a descrição do produto"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={description}
                onChangeText={setDescription}
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