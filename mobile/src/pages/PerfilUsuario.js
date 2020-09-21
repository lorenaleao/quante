import React, { useState } from 'react';
import { Alert, StyleSheet, Text, Image, View, StatusBar, TouchableOpacity } from 'react-native';
import {MaterialIcons} from '@expo/vector-icons';

function CadastraUsuario({navigation}){

  const [usuario, setUsr] = useState({});

  async function getUsuario(){
    //const response = await api.get('', {params: {cpf}})
    const response = {
        data:{id: 0, name:'Cliente A', cpf: '123.456.789-10', regDate: "23/09/2020", contribuiu:'5', lastSup:"Supermercado BH", lastProd:"Yakult", pic:'https://eshendetesia.com/images/user-profile.png'}
    }
    setUsr(response.data);
  }

  async function deleteUsuario(){
    Alert.alert(
      'Deletar Conta?', 'Você deseja deletar a sua conta do nosso aplicativo junto com todo o seu histórico de contribuições?',
      [{text: 'Cancelar', onPress: () => console.log("Cancel Pressed"),},
    {text: 'Apagar', onPress: () => {
      //const response = await api.delete('', {params: {cpf}})
      console.log("Apagou")
    }}]
  )
    
  }

  async function logout(){
    Alert.alert(
      'Logout?', 'Você deseja sair da sua conta?',
      [{text: 'Cancelar', onPress: () => console.log("Cancel Pressed"),},
    {text: 'Logout', onPress: () => {
      //const response = await api.delete('', {params: {cpf}})
      console.log("Saiu")
    }}]
  )
    
  }

    if(JSON.stringify(usuario) === JSON.stringify({})){
      getUsuario();
    }


    return (
        <>
        <View style={styles.cabecalho}/>
        <View style={styles.borda}/>
        <Image source={{uri: usuario.pic}} style={styles.fotoPerfil} />
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>Nome: </Text>
            <Text>{usuario.name}</Text>
        </View>
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>CPF: </Text>
            <Text>{usuario.cpf}</Text>
        </View>
        <View style={styles.campoTexto}>
            <View style={styles.box}>
              <Text style={styles.textoLabel}>Contribuições:</Text>
              <Text>{usuario.contribuiu}</Text>
            </View>
            <View style={styles.box}>
              <Text style={styles.textoLabel}>Última Contribuição:</Text>
              <Text>{usuario.lastSup}</Text>
              <Text>{usuario.lastProd}</Text>
            </View>
        </View>
        <View style={styles.botoesMenu}>
          <TouchableOpacity style={styles.deleteButton}>
          <MaterialIcons name="delete" size={20} onPress={deleteUsuario} color={"#fff"} />
          </TouchableOpacity>
          <TouchableOpacity style={styles.deleteButton}>
          <MaterialIcons name="exit-to-app" size={20} onPress={logout} color={"#fff"} />
          </TouchableOpacity>
        </View>
        
        </>
    )

}


const styles = StyleSheet.create({
  cabecalho: {
    width: '100%',
    height: '20%',
    backgroundColor: '#87ceeb',
    alignItems: 'center',
    justifyContent: 'center',
  },
  fotoPerfil: {
      position: 'absolute',
      top: '10%',
      left: '35%',
      width: '30%',
      aspectRatio: 1,
      zIndex: 5,
  },
  borda:{
    position: 'absolute',
    top: '8.5%',
    left: '32.5%',
    backgroundColor: '#FFF',
    width: '35%',
    aspectRatio: 1,
    borderRadius: 100,
    zIndex: 4,
  },
  campoTexto: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    top: 80
  },
  textoLabel:{
    fontWeight: 'bold'
  },
  box: {
    width: '43%',
    aspectRatio: 1.2,
    backgroundColor: '#FFF',
    margin: 5,
    top: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  deleteButton: {
    width: 50,
    height: 50,
    backgroundColor: '#1e5bc6',
    borderRadius: 25,
    justifyContent: 'center',
    alignItems: 'center',
    right: 10,
    bottom: 10,
    margin: 5
  },
  botoesMenu: {
    width: 110,
    alignSelf: 'flex-end',
    position: 'absolute',
    right: 10,
    bottom: 10,
    flexDirection: 'row',
  }
});

export default CadastraUsuario;