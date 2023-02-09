Nombre: tomas
commands:
        estas ahi
        reproduce (en youtube)
        que
            hora
            dia
        busca informacion de (en wikipedia)
        busca en internet (URLS)
        busca en google (websearch open)
        descansa
openai response if not understand command

            # old functions
            
            # elif 'calculadora' in rec:
            #     speak('que operacion quieres hacer')
            #     listen()
            #     order = rec.replace('resultado', '')
            #     numbers=order.split('+').split('-').split('*').split('/')
            #     numberone=numbers[0].replace(' ','')
            #     numbertwo=numbers[1].replace(' ','')
            #     print(f'operacion es {order}')
            #     speak(f'operacion es {order}')                

            # elif 'busca informacion de' in rec:
            #     order = rec.replace('busca informacion de', '')
            #     speak(f"Ok, searching about {order}")
            #     engine.setProperty('rate', 110)
            #     wikipedia.set_lang("es")
            #     info = wikipedia.summary(order, 1)
            #     speak(info)
            #     return init_waiting()
            
            # elif 'busca en internet' in rec:
            #     order= rec.replace('busca en internet','')
            #     speak(f'okay there is the first results i found about {order}')
            #     results = search(f"{order}",num_results = 5)
            #     for result in results:
            #         result = result.replace('https','').replace('http','').replace('://','').replace('www.','')
            #         speak(result)
            #         print(result)

