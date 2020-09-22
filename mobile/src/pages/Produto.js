import React, { useState } from 'react';
import { Alert, StyleSheet, ScrollView, SafeAreaView, Text, Image, View, StatusBar, TouchableOpacity } from 'react-native';
import {MaterialIcons} from '@expo/vector-icons';

function Produto({route, navigation}){

    const [produto, setProd] = useState({});
    const [reviews, setReview] = useState([]);

    async function getProduto(){
        //const response = await api.get('', {params: {textoBusca}})
        var response
        if(parseInt(route.params.id)%2 == 0){
            response = {
                data:{id: 0, name:'Yakult', description: 'L. casei Shirota contribui para o equilíbrio da flora intestinal. Porção de 80 g', category:'Frios, Iogurtes e Laticínios' ,pic:'https://api.tendaatacado.com.br/fotos/1209.jpg', prices:{SupermercadoBH:'R$7,90', Carrefour:'R$11,49',Extra:'R$8,00', Dia: 'R$8,50','Super Nosso':'R$8,50'}}
            }
        } else {
            response = {
                data:{id: 1, name:'Yakult Desnatado', description: 'Leite Fermentado Desnatado Light 40, da Yakult. Porção de 80 g ', category:'Frios, Iogurtes e Laticínios', pic:'https://static.carrefour.com.br/medias/sys_master/images/images/h8b/hb0/h00/h00/9458275549214.jpg', prices:{SupermercadoBH:'R$7,90', Carrefour:'R$11,49',Extra:'R$8,00', Dia: 'R$8,50','Super Nosso':'R$8,50'}}
            }
        }
        setProd(response.data);
    }

    async function getReviews(){
        //const response = await api.get('', {params: {produto.id}})
        const response = {
            data:[
                {review_autor:"Cliente A", review_rating:"5.0", review_text:"Compro pra minha filha toda semana, e graças a esse app eu não compro mais caro no Carrefour.", published_date:"22/09/2020", is_recommended:true, likes:5},
                {review_autor:"Cliente A", review_rating:"5.0", review_text:"Compro pra minha filha toda semana, e graças a esse app eu não compro mais caro no Carrefour.", published_date:"22/09/2020", is_recommended:false, likes:5},
                {review_autor:"Cliente A", review_rating:"5.0", review_text:"Compro pra minha filha toda semana, e graças a esse app eu não compro mais caro no Carrefour.", published_date:"22/09/2020", is_recommended:true, likes:5},
                {review_autor:"Cliente A", review_rating:"5.0", review_text:"Compro pra minha filha toda semana, e graças a esse app eu não compro mais caro no Carrefour.", published_date:"22/09/2020", is_recommended:false, likes:5},
            ]
        }
        setReview(response.data);
    }

    if(JSON.stringify(produto) === JSON.stringify({})){
        getProduto();
        getReviews();
    }
  
    console.log(reviews);

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
            <ScrollView contentContainerStyle={styles.containerListaPrecos} style={styles.listaPrecos} >
                {JSON.stringify(produto) != JSON.stringify({}) && Object.keys(produto.prices).map((prop, key) => {
                    return (
                    <TouchableOpacity key={key} style={styles.itemPrecos} >
                        <Text style={styles.textoMercado}>{prop}</Text>
                        <Text style={styles.textoPreco}>{produto.prices[prop]}</Text>
                    </TouchableOpacity>
                    ); 
                })} 
            </ScrollView>
        </SafeAreaView>
        <View style={{backgroundColor:'white', flexDirection:'row'}}>
            <Text style={styles.titulo}>Avaliações Deste Produto:</Text>
            <TouchableOpacity style={styles.botaoAdicionaReview} >
                    <Text style={{color:'white'}}>Avaliar Produto</Text>
            </TouchableOpacity>
        </View>       
        <SafeAreaView>
            <ScrollView style={styles.listaReviews} >
                {reviews.length > 0 && reviews.map((prop, key) => {
                    return (
                    <View key={key} style={styles.itemReview} >
                        <View style={styles.ladoA}>
                            {prop.is_recommended && <MaterialIcons name="thumb-up" size={20} color={"green"} />}
                            {!prop.is_recommended && <MaterialIcons name="thumb-down" size={20} color={"red"} />}
                            <TouchableOpacity style={styles.botaoCurtir} >
                                <Text style={{color:'white'}}>Curtir</Text>
                            </TouchableOpacity>
                        </View>
                        <View style={styles.ladoB}>
                            <Text>{prop.review_text}</Text>
                            <Text style={styles.rodapeReview}>Postada por {prop.review_autor}, em {prop.published_date}</Text>
                        </View>
                    </View>
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
  titulo:{
      fontWeight: "bold",
      backgroundColor: 'white',
      fontSize: 16,
      padding: 10
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
  containerListaPrecos:{
    justifyContent: 'center',
    alignItems: 'center', 
  },
  listaPrecos:{
    width: '100%',
    height: '33%',
    backgroundColor: "#FFF"
  },
  listaReviews:{
    width: '100%',
    height: '26%',
    backgroundColor: "#FFF"
  },
  textoMercado: {
    width: '45%',
    height: 40,
    marginLeft: 5,
    marginTop: 5,
    marginBottom: 5,
    textAlign: 'center',
    backgroundColor: "#1e5bc6",
    color: 'white'     
},
textoPreco: {
    width: '45%',
    height: 40,
    marginRight: 5,
    marginTop: 5,
    marginBottom: 5,
    textAlign: 'center',
    backgroundColor: "#1e5bc6",
    color: 'white'
},
  itemPrecos:{
      flex: 1,
      flexDirection: 'row',
      justifyContent: 'center',
      alignItems: 'center', 
  },
  itemReview:{
      flexDirection:'row',
      flexWrap: 'wrap',
      margin: 5,
      borderBottomColor: 'black',
      borderBottomWidth: 1,
    },
    ladoA:{
        width:'20%',
        alignItems: 'center',
        justifyContent: 'center',
    },
    ladoB:{
        width:'80%'
    },
  rodapeReview: {
      fontStyle: 'italic',
      marginTop: 5,
      paddingBottom: 5
  },
  botaoAdicionaReview:{
      backgroundColor: "#1e5bc6",
      width:120,
      height: 30,
      borderRadius: 25,
      marginLeft: 5,
      marginTop: 5,
      flexDirection: 'row',
      alignContent: 'center',
      alignItems: 'center',
      justifyContent: 'center',
  },
  botaoCurtir:{
      marginTop: 15,
      backgroundColor: "#1e5bc6",
      paddingHorizontal: 10,
      paddingVertical:5,
      borderRadius: 25
  }
});

export default Produto;