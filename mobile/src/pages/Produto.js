import React, { useState } from 'react';
import { Alert, StyleSheet, ScrollView, SafeAreaView, Text, Image, View, StatusBar, TouchableOpacity } from 'react-native';
import {MaterialIcons} from '@expo/vector-icons';

function Produto({route, navigation}){

    const [produto, setProd] = useState({});

    async function procuraNoBanco(){
        //const response = await api.get('', {params: {textoBusca}})
        var response
        if(parseInt(route.params.id)%2 == 0){
            response = {
                data:{id: 0, name:'Yakult', description: 'L. casei Shirota contribui para o equilíbrio da flora intestinal. Porção de 80 g', category:'Frios, Iogurtes e Laticínios' ,pic:'https://api.tendaatacado.com.br/fotos/1209.jpg', price:{SupermercadoBH:'R$7,90', Carrefour:'R$11,49'}}
            }
        } else {
            response = {
                data:{id: 1, name:'Yakult Desnatado', description: 'Leite Fermentado Desnatado Light 40, da Yakult. Porção de 80 g ', category:'Frios, Iogurtes e Laticínios', pic:'https://static.carrefour.com.br/medias/sys_master/images/images/h8b/hb0/h00/h00/9458275549214.jpg'}
            }
        }
        setProd(response.data);
    }

    if(JSON.stringify(produto) === JSON.stringify({})){
        procuraNoBanco();
    }
  
    console.log(produto);

    return (
        <>
        <View style={styles.cabecalho}>
            <Image source={{uri: produto.pic}} style={styles.fotoProduto} />
            <View style={styles.fichaTecnica}>
                <Text style={styles.textoLabel}>Nome:</Text>
                <Text style={styles.campoTexto}>{produto.name}</Text>
                <Text style={styles.textoLabel}>Descrição:</Text>
                <Text style={styles.campoTexto}>{produto.description}</Text>
                <Text style={styles.textoLabel}>Categoria:</Text>
                <Text>{produto.category}</Text>
            </View>
        </View>
        <SafeAreaView>
            <ScrollView contentContainerStyle={styles.containerListaProdutos} style={styles.listaProdutos} >
                {produto.prices.map((prop, key) => {
                    return (
                    <TouchableOpacity style={styles.itemProduto} >
                        <Text>Supermercado {key}</Text>
                        <Text>Preço {prop}</Text>
                    </TouchableOpacity>
                    );
                })} 
            </ScrollView>
        </SafeAreaView>
        </>
    )


}


const styles = StyleSheet.create({
  cabecalho:{
      height: '33%',
      backgroundColor: '#FFF',
      flexDirection: 'row',
  },
  fotoProduto:{
    height: '80%',
    aspectRatio: 1,
    top: '5%',
    left: 5
  },
  fichaTecnica: {
    width: '50%',
    marginLeft: '5%',
    marginTop: 20,
  }, 
  campoTexto: {
    textAlign: 'justify'
  },
  textoLabel:{
    fontWeight: 'bold'
  },
  containerListaProdutos:{},
  listaProdutos:{}
});

export default Produto;