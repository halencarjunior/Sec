#include <tins/tins.h>
#include <cassert>
#include <iostream>
#include <string>

using namespace Tins;

int main() {

    NetworkInterface iface = NetworkInterface::default_interface();
    NetworkInterface::Info info = iface.addresses();
PacketSender sender;

    //std::cout << iface << std::endl;
    //std::cout << info << std::endl;

    // same as above, just shorter
    IP pacote = IP("192.168.1.1") /
                     TCP(80, 10000);
                     //RawPDU("I'm a payload!");
    pacote.rfind_pdu<TCP>().set_flag(TCP::SYN, 1);    
   
    // Send and receive the response.
    std::unique_ptr<PDU> response(sender.send_recv(pacote));
    // Did we receive anything?
    if (response) {
        TCP &tcp = response->rfind_pdu<TCP>();
            if (tcp.get_flag(TCP::RST)) { 
                std::cout << "Port is closed!" << std::endl;
            }
            else {
                std::cout << "Port is open!" << std::endl;
            }
    }


//    PacketSender sender;
//    sender.send(pacote, iface);
}
