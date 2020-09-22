import React, { useState } from 'react';
import {Image, View, ScrollView, SafeAreaView, Text, TextInput, TouchableOpacity, StyleSheet, Picker} from 'react-native';
import {MaterialIcons} from '@expo/vector-icons'
import { set } from 'react-native-reanimated';

import api from '../services/api';

function BuscaProduto({navigation}){
    const [produtos, setProd] = useState([]);
    const [textoBusca, setTextobusca] = useState('');
    const [selectedValue, setSelectedValue] = useState("java");

    async function procuraNoBanco(){

        const resp = await api.get('product/get/substr/'+textoBusca,).then((response) => {
            setProd(response.data)
        })
    }

    return (
        <View style={{flex:1}}>
            <View style={styles.searchForm}>
                <TextInput 
                style = {styles.searchInput}
                placeholder="Insira o nome do produto"
                placeholderTextColor="#999"
                autoCapitalize="words"
                autoCorrect={false}
                value={textoBusca}
                onChangeText={setTextobusca}
                />

                <TouchableOpacity style={styles.loadButton}>
                    <MaterialIcons name="search" size={20} onPress={procuraNoBanco} color={"#fff"} />
                </TouchableOpacity>
            </View>
            <View style={styles.menuPesquisa}>
                <Text>Ordenar Por:</Text>
                <Picker
                    selectedValue={selectedValue}
                    style={styles.listaOrdena}
                    onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
                >
                    <Picker.Item label="Nenhum" value="null" />
                    <Picker.Item label="Nome" value="nome" />
                    <Picker.Item label="Preço Mínimo" value="pmin"/>
                </Picker>
            </View>
            <SafeAreaView>
                <ScrollView contentContainerStyle={styles.containerListaProdutos} style={styles.listaProdutos} >
                    {produtos != [] && produtos.map((prop, key) => {
                        console.log(prop);
                        return (
                        <TouchableOpacity style={styles.itemProduto}  onPress={() => navigation.navigate('Produto', {id:prop._id})}>
                            <Image source={{uri: 'https://vivanosports.com.br/images/sem_foto.png'}} style={styles.fotoProduto} />
                            <Text>{prop.name}</Text>
                            <Text>Preço Mín: {prop.prices[Object.keys(prop.prices)[0]][1][0]}</Text>
                            <Text>Preço Max: {prop.prices[Object.keys(prop.prices)[0]][1][1]}</Text>
                        </TouchableOpacity>
                        );
                    })} 
                </ScrollView>
            </SafeAreaView>
        </View>
    );

    function ordenaPor(init, fim){
        var i = init;
        var j = fim;
        const meio = ((init + fim) /2) >> 0;
        pivo = produtos[meio];
        while( i <= j){
            while (produtos[i] < pivo)
                i++;
            while(produtos[j] > pivo)
                j++;
            if(i <= j){
                aux = produtos[i]
                
            }
        }
    }
}

const styles = StyleSheet.create({
    searchForm: {
        position: 'absolute',
        top: 20,
        left: 20,
        right: 20,
        zIndex: 5,
        flexDirection: 'row',
    },

    searchInput: {
        flex: 1,
        height: 50,
        backgroundColor: '#FFF',
        color: '#333',
        borderRadius: 25,
        paddingHorizontal: 20,
        fontSize: 16,
        shadowColor: '#000',
        shadowOpacity: 0.2,
        shadowOffset: {
            width: 4,
            height: 4,
        },
        elevation: 2,
    },

    loadButton: {
        width: 50,
        height: 50,
        backgroundColor: '#1e5bc6',
        borderRadius: 25,
        justifyContent: 'center',
        alignItems: 'center',
        marginLeft:  15,
    },

    listaProdutos:{
        top: 100,
        width: '100%',
        height: '75%',
    },

    containerListaProdutos:{
        flexGrow:1, 
        flexDirection: 'row', 
        flexWrap: 'wrap', 
        justifyContent: 'center',
        alignItems: 'center', 
    },

    itemProduto:{
        margin: '3%',
        width: '40%',
        justifyContent: 'center',
        alignItems: 'center',
        aspectRatio: 0.7,
        backgroundColor: '#FFF',
    },

    fotoProduto: {
        width: '80%',
        aspectRatio: 1,
    },

    menuPesquisa: {
        top: 80,
        marginLeft:'40%',
        flexDirection: 'row', 
    },

    listaOrdena: { 
        height: 20, 
        width: 120, 
        marginLeft: 10, 
        backgroundColor:'white'
    }
});

export default BuscaProduto;