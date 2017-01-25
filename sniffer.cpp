#include <iostream>
#include <tins/tins.h>
 
using namespace Tins;
  
bool callback(const PDU &pdu) {
    const IP &ip = pdu.rfind_pdu<IP>();
    const TCP &tcp = pdu.rfind_pdu<TCP>();
    std::cout << ip.src_addr() << ':' << tcp.sport() << " -> " << ip.dst_addr() << ':' << tcp.dport() << std::endl;
    return true;
}

int main(int argc, char* argv[]) {


  if (argc != 2) {
        std::cout << "Usage: sudo ./sniffer <interface>" << std::endl;
        return 1;
    }

      Sniffer sniffer(argv[1], 2000);
      sniffer.sniff_loop(callback);
    
}
