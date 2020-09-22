import React, { useState } from 'react';
import { Alert, StyleSheet, Text, Image, View, StatusBar, TouchableOpacity } from 'react-native';
import {MaterialIcons} from '@expo/vector-icons';
import { TextInput } from 'react-native-gesture-handler';

import api from '../services/api';

function PerfilUsuario({route, navigation}){

  const [usuario, setUsr] = useState({});
  //const usrID = route.params.uID;
  const usrID = '5f6a2f7dd2c784e8ef49ef5d';

  async function getUsuario(){
    console.log('ID:' + usrID);
    const getBanco = await api.get('client/get/5f6a2f7dd2c784e8ef49ef5d',).then((resp) => {
        setUsr(resp.data)
    })
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
        <Image source={{uri: 'https://eshendetesia.com/images/user-profile.png'}} style={styles.fotoPerfil} />
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>Nome: </Text>
            <TextInput>{usuario.name}</TextInput>
        </View>
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>Idade: </Text>
            <TextInput>{usuario.age}</TextInput>
        </View>
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>CPF: </Text>
            <TextInput>{usuario.cpf}</TextInput>
        </View>
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>Email: </Text>
            <TextInput>{usuario.email}</TextInput>
        </View>
        <View style={styles.campoTexto}>
            <Text style={styles.textoLabel}>Senha: </Text>
            <TextInput secureTextEntry={true}>{usuario.password}</TextInput>
        </View>
        <View style={styles.campoTexto}>
            <View style={styles.box}>
              <Text style={styles.textoLabel}>Avaliações:</Text>
              <Text>5</Text>
            </View>
            <View style={styles.box}>
              <Text style={styles.textoLabel}>Última Avaliação:</Text>
              <Text>Yakult</Text>
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

export default PerfilUsuario;