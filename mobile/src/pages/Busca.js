import React, { useState } from 'react';
import {Image, View, ScrollView, SafeAreaView, Text, TextInput, TouchableOpacity, StyleSheet, Picker} from 'react-native';
import {MaterialIcons} from '@expo/vector-icons'
import { set } from 'react-native-reanimated';

function BuscaProduto({navigation}){
    const [produtos, setProd] = useState([]);
    const [textoBusca, setTextobusca] = useState('');
    const [selectedValue, setSelectedValue] = useState("java");

    async function procuraNoBanco(){
        //const response = await api.get('', {params: {textoBusca}})
        const response = {
            data:[
                {id: 0, name:'Yakult', priceMin: 'R$7,90', priceMax:'R$11,49' ,pic:'https://api.tendaatacado.com.br/fotos/1209.jpg'},
                {id: 1, name:'Yakult Desnatado', priceMin: 'R$ 10,29', priceMax:'R$12,89', pic:'https://static.carrefour.com.br/medias/sys_master/images/images/h8b/hb0/h00/h00/9458275549214.jpg'},
                {id: 2, name:'Yakult', priceMin: 'R$7,90', priceMax:'R$11,49' ,pic:'https://api.tendaatacado.com.br/fotos/1209.jpg'},
                {id: 3, name:'Yakult Desnatado', priceMin: 'R$ 10,29', priceMax:'R$12,89', pic:'https://static.carrefour.com.br/medias/sys_master/images/images/h8b/hb0/h00/h00/9458275549214.jpg'},
                {id: 4, name:'Yakult', priceMin: 'R$7,90', priceMax:'R$11,49' ,pic:'https://api.tendaatacado.com.br/fotos/1209.jpg'},
                {id: 5, name:'Yakult Desnatado', priceMin: 'R$ 10,29', priceMax:'R$12,89', pic:'https://static.carrefour.com.br/medias/sys_master/images/images/h8b/hb0/h00/h00/9458275549214.jpg'},
            ]
        }
        setProd(response.data);
        console.log("Deu o response");
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
                    {produtos.map((prop) => {
                        return (
                        <TouchableOpacity key={prop.id} style={styles.itemProduto}  onPress={() => navigation.navigate('Produto', {id:prop.id})}>
                            <Image source={{uri: prop.pic}} style={styles.fotoProduto} />
                            <Text>{prop.name}</Text>
                            <Text>Preço Mín: {prop.priceMin}</Text>
                            <Text>Preço Max: {prop.priceMax}</Text>
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