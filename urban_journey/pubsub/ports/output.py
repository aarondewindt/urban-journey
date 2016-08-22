from urban_journey.pubsub.ports.base import PortBase
from urban_journey.pubsub.descriptor.instance import DescriptorInstance
from urban_journey.pubsub.descriptor.static import DescriptorStatic


def Output(channel_name=None,
           auto_connect=True):
    return DescriptorStatic(OutputPort,
                            channel_name=channel_name,
                            auto_connect=auto_connect)


class OutputPort(PortBase, DescriptorInstance):
    def __init__(self,
                 parent_object,
                 attribute_name,
                 channel_name=None,
                 auto_connect=True):
        """
        :param parent_object: ModelBase instance that owns this port
        :param attribute_name: Name of this port inside the model ase instance
        :param channel_name: Optional. Channel name to connect to. If None, attribute name will be used as channel_name.
        :param auto_connect: True to automatically connect to a channel.
        """

        PortBase.__init__(self, parent_object, attribute_name, channel_name, auto_connect)
        DescriptorInstance.__init__(self, parent_object, attribute_name)

        self.filters = []

    async def flush(self, data):
        print("OutputPort.flush({})".format(data))
        await self.channel.flush(data)
